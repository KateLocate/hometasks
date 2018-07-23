# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil


def make_dir(name, n=1):
    if n > 1:
        for i in range(n):
            dir_path = os.path.join(os.getcwd(), name+str(n - i))
            try:
                os.mkdir(dir_path)
            except FileExistsError:
                print('Директория с таким именем уже есть в данной папке!')
            except NameError:
                print('Укажите имя файла в кавычках!')
    else:
        dir_path = os.path.join(os.getcwd(), name)
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print('Директория с таким именем уже есть в данной папке!')
        except NameError:
            print('Укажите имя файла в кавычках!')


def remove_dir(name, n=1):
    if n > 1:
        for i in range(n):
            try:
                os.removedirs(str(os.getcwd())+'\\'+name+str(n - i))
            except FileNotFoundError:
                print('Вы пытаетесь удалить несуществующую директорию!')
            except NameError:
                print('Укажите имя файла в кавычках!')
    else:
        try:
            os.removedirs(str(os.getcwd())+'\\'+name)
        except FileNotFoundError:
            print('Вы пытаетесь удалить несуществующую директорию!')
        except NameError:
            print('Укажите имя файла в кавычках!')


make_dir('dir_', 9)
remove_dir('dir_', 9)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def current_directory_files():
    print(os.listdir(os.getcwd()))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def current_file_copy():
    return shutil.copyfile(os.path.realpath(__file__), str(os.path.realpath(__file__)[:-3])+'_copy.py')
