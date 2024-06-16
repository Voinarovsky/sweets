import os
import tempfile
from vosk_tts import Model, Synth
from pydub import AudioSegment
from pydub.playback import play


class Voice:
    def __init__(self):
        model = Model(model_name='vosk-model-tts-ru-0.6-multi')
        self.synth = Synth(model)
        self.speaker = 3

    def text_to_speech(self, text='Добрый день!'):
        # Используем временную директорию для хранения файла
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
            tmp_file_path = tmp_file.name
        self.synth.synth(text, tmp_file_path, speaker_id=self.speaker)

        # Загружаем аудио файл и воспроизводим его
        sound = AudioSegment.from_wav(tmp_file_path)
        play(sound)

        # Удаляем временный файл после воспроизведения
        os.remove(tmp_file_path)

    def set_voice(self, speaker):
        self.speaker = speaker


voice = Voice()
if __name__ == '__main__':
    voice.text_to_speech()

