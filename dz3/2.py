
def json2yaml(json_file):
    import json
    import yaml
    from pathlib import Path
    # Открываем и читаем json-файл
    with open(json_file, 'r') as f: #использую with что бы автоматически закрывать файл
        json_data = json.load(f)

    # Устанавливаем путь и имя файла yaml
    yaml_file = Path(json_file).with_suffix('.yaml') #преобразуем путь к файлу json в путь к файлу yaml, заменяя расширение файла на .yaml

    # Записываем данные в yaml-файл
    with open(yaml_file, 'w') as f:
        yaml.dump(json_data, f)

    # Возвращаем прочитанные данные
    return json_data

data = json2yaml('sample1.json')
print(data)  # Выводим прочитанные данные в формате JSON
