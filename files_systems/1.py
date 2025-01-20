import os


def search_files():
    # path_file = 'D://projects/laba_python/files_systems/test_1'
    # expansion = '.py'
    path_file = input('Введите путь: ')
    expansion = input('Введите расширение: ')
    for currentdir, dirs, files in os.walk(path_file):
        for file in files:
            if os.path.splitext(file)[-1] == expansion:
                print(f'{currentdir}/{file}'.replace("\\", "/"))


if __name__ == "__main__":
    search_files()
