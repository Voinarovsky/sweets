from handlers import thanks, music_YouTube, stop, get_weather, orel_rehka, get_currency_rates, my_wave
from voice import voice


COMMANDS = [
    {'id': 0, 'text': 'спасибо', 'handler':thanks},
    {'id': 1, 'text': 'включи музыку для фона', 'handler':music_YouTube},
    {'id': 3, 'text': 'останови все', 'handler':stop},
    {'id': 4, 'text': 'какая сейчас температура', 'handler': get_weather},
    {'id': 5, 'text': 'брось монетку', 'handler': orel_rehka},
    {'id': 6, 'text': 'какой курс', 'handler': get_currency_rates},
    {'id': 7, 'text': 'включи мою волну', 'handler': my_wave},
]
ACTIVATION = 'джарвис'
class Command:

    def __init__(self,text):
        self.text = text
        self.map()

    def map(self):
        if self.text.startswith(ACTIVATION):
            self.text = self.text.replace(ACTIVATION, '').strip()
            for cmd in COMMANDS:
                if self.text.startswith(cmd['text']):
                    self.run(cmd)
                    return True
            else:
                voice.text_to_speech('Возможно я не распознала команду, повторите пожалуйста.')

    def run(self,cmd):
        handler = cmd['handler']
        handler(self.text)