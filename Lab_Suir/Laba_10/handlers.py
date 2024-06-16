import random
import time
from voice import voice
import webbrowser
import pyautogui
import sys
import requests

def thanks(text):
    options = [
        'Обращайтесь!',
        'Всегда к вашим услугам!',
        'Подсказать что нибудь еще?',
        'Спасибо на хлеб не намажешь! Шутка! Всегда пожалуйста!',
        'Пожалуйста! Рад был помочь.'
    ]

    sel = random.choice(options)
    voice.text_to_speech(sel)

def music_YouTube(text):
    options = [
        'открываю YouTube для фоновой музыки. Приятного прослушивания!',
        'С радостью! Сейчас открою YouTube для фоновой музыки.',
        'Конечно, включаю YouTube с фоновой музыкой. Наслаждайтесь!',
        'С удовольствием! Вот ваша фоновая музыка на YouTube.',
        'Без проблем! Открываю YouTube с фоновой музыкой для вас.'
    ]
    sel = random.choice(options)
    voice.text_to_speech(sel)
    time.sleep(0.5)
    webbrowser.open('https://www.youtube.com/watch?v=4xDzrJKXOOY')

def stop(text):
    options = [
        'Без проблем, прекращаю работу. До новых встреч!',
        'Выполняю, все процессы остановлены. Обращайтесь, если снова понадобится моя помощь!',
        'Конечно, останавливаю все процессы. Если понадобится помощь, обращайтесь!',
        'Понял, ассистент прекращает работу. Всегда готов помочь снова!',
        'Хорошо, останавливаю выполнение задач. Жду ваших новых команд!'
    ]
    sel = random.choice(options)
    voice.text_to_speech(sel)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'w')
    sys.exit()


def get_weather(text):
    api_key = 'c9c4d34f92b5a7ae386515d0c436f59a'
    # URL для получения погоды в Санкт-Петербурге
    url = f'http://api.openweathermap.org/data/2.5/weather?q=Saint Petersburg,RU&units=metric&appid={api_key}'

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    temperature = str(data['main']['temp'])
    options = [
        'Вот погода в санкт-петербурге сейчас. Я вывел ее вам на экран!',
        'На улице в Санкт-Петербурге сейчас жарко. Погоду я отобразил на экране, можете проверить.',
        'Погода выведена на экран, приятного дня!',
    ]
    sel = random.choice(options)
    voice.text_to_speech(sel)
    print(f'В Санкт-Петербурге сейчас {temperature}°C')

def orel_rehka(text):
    monetka = random.randint(1,2)
    if monetka == 1:
        options = 'Выпала решка!'
    else:
        options = 'Выпал орел!'
    voice.text_to_speech(options)

def get_currency_rates(text):
    options = [
        'Вот курс евро и курс доллара. Я вывел ее вам на экран!',
        'Ну и треш. Курс евро и доллара я отобразил на экране. Извините, говорить такие числа вслух страшно.'
    ]
    sel = random.choice(options)
    voice.text_to_speech(sel)

    # Запрос к API Центрального банка России для получения курсов валют
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    response.raise_for_status()

    # Парсинг JSON ответа
    data = response.json()

    # Извлечение курсов евро и доллара
    usd_rate = data['Valute']['USD']['Value']
    eur_rate = data['Valute']['EUR']['Value']

    print(f"Курс доллара (USD): {usd_rate} рублей")
    print(f"Курс евро (EUR): {eur_rate} рублей")

def my_wave(text):
    options = [
        'Включаю мою волну!',
        'послушаем вашу любимую музыку!',
        'Включаю мою любимую музыку!',
        'Я конечно не Алиса но волну тоже могу включить!'
    ]
    sel = random.choice(options)
    voice.text_to_speech(sel)
    time.sleep(0.5)
    webbrowser.open('https://music.yandex.ru/home?utm_source=services&utm_medium=dstore_bro&utm_campaign=general_ru_desktop_no_all')
    time.sleep(4)
    pyautogui.press('p')