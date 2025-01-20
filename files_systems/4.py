import os


def add_in_collections(data, libraries_from, libraries_usually):
    for elem in data:
        elem = elem.split()
        if elem:
            if elem[0] == 'import':
                for lib in elem[1:]:
                    lib = lib.replace(',', '')  # случай, если через import сделали несколько библиотек
                    libraries_usually.add(lib)
            elif elem[0] == 'from':
                if elem[1] not in libraries_from:
                    libraries_from[elem[1]] = set()
                for lib in elem[3:]:
                    lib = lib.replace(',', '')  # случай, если через from несколько импортов в одной строке
                    libraries_from[elem[1]].add(lib)
    return libraries_from, libraries_usually


def make_imports():
    # full_path = "D://projects/laba_python/files_systems/test_4"
    full_path = input('Введите путь: ')

    if not os.path.isdir(full_path):
        print('нет src путя')
        return

    libraries_from = {}
    libraries_usually = set()

    for currentdir, dirs, files in os.walk(full_path):
        for file in files:
            path_file = os.path.join(currentdir, file)
            if os.path.splitext(path_file)[-1] == '.py':
                with open(path_file, mode='r', encoding='utf-8') as file_py:
                    data = file_py.readlines()
                libraries_from, libraries_usually = add_in_collections(data, libraries_from, libraries_usually)

    with open('res_4.py', mode='w', encoding='utf-8') as file:
        for lib in libraries_usually:
            file.write(f'import {lib}\n')
        for lib in libraries_from:
            file.write(f'from {lib} import {", ".join(libraries_from[lib])}\n')


if __name__ == "__main__":
    make_imports()
