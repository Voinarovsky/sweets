def json2yaml(filename: str):
    import json
    import yaml
    from pathlib import Path
    # Открываем и читаем json-файл
    with open(filename, 'r') as f: #использую with что бы автоматически закрывать файл
        json_data = json.load(f)

    # Устанавливаем путь и имя файла yaml
    yaml_file = Path(filename).with_suffix('.yaml') #преобразуем путь к файлу json в путь к файлу yaml, заменяя расширение файла на .yaml

    # Записываем данные в yaml-файл
    with open(yaml_file, 'w') as f:
        yaml.dump(json_data, f)

    # Возвращаем прочитанные данные
    return json2yaml

print(json2yaml())