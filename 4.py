# Разработайте скрипт, который выводит список файлов в указанной директории
# и информацию о каждом файле (например, размер, дата создания и т. д.).
# Для этого используйте модуль os или os.path.

import os

# var
path = ""


# def
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


# main
print("Enter path: ")
path = input()
for file in files("."):  
    print(file)
    status = os.stat(file)
    print(f"The size of the file '{file}' is {status.st_size} bytes.")
    print(f"The time of most recent content modification in '{file}' is {status.st_mtime} seconds.")
