def unix2dos(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    content = content.replace('\n', '\r\n')

    with open(file_path, 'w') as file:
        file.write(content)

unix2dos('1.txt')
