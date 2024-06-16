import requests


def get_currency_rates():
    options = [
        'Вот курс евро и курс доллара. Я вывел ее вам на экран!',
        'Ну и треш. Курс евро и доллара я отобразил на экране. Извините, говорить такие числа вслух страшно.'
    ]

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

get_currency_rates()