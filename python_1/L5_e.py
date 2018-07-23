# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil


def duplicate_dir(n=1):
    for i in range(n):
        dir_path = os.path.join(os.getcwd(), 'dir_'+str(n - i))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print('Директория с таким именем уже есть в данной папке!')


def remove_duplicated_dir(n=1):
    for i in range(n):
        try:
            os.removedirs(str(os.getcwd())+'\\'+'dir_'+str(n - i))
        except FileNotFoundError:
            print('Вы пытаетесь удалить несуществующую директорию!')


duplicate_dir(9)
remove_duplicated_dir(9)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def current_directory_files():
    print(os.listdir(os.getcwd()))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def current_file_copy():
    return shutil.copyfile(os.path.realpath(__file__), str(os.path.realpath(__file__)[:-3])+'_copy.py')
