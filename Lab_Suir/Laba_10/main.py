import time
from recognition import Recognaizer
from voice import voice
from commands import Command

rec = Recognaizer()
text_gen = rec.listen()
rec.stream.stop_stream()
voice.text_to_speech('Привет, меня зовут джарвис! Что вам подсказать?')
print('Могу включить музыку для работы - "включи музыку для фона"')
print('Скажу какая сейчас температура в Санкт-Петербурге - "какая сейчас температура"')
print('Не можете принять решение? - "брось монетку"')
print('расскажу курс Евро и Доллара - "какой курс"')
print('Хотите включу вашу любимую музыку? - "включи мою волну"')
print('Завершить сеанс - "стоп"')
print('Незабыть сказать мне спасибо - "спасибо"')
print('------------------------')
print('↓↓↓ ИСТОРИЯ ЗАПРОСОВ ↓↓↓')
time.sleep(0.5)
rec.stream.start_stream()

for text in text_gen:
    print(text)

    rec.stream.stop_stream()
    Command(text)
    time.sleep(0.5)
    rec.stream.start_stream()