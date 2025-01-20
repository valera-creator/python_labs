import os
import shutil


def search_size_files():
    # full_path_file = 'D://projects/laba_python/files_systems/test_2.zip'
    full_path_file = input('Введите путь: ')
    shutil.unpack_archive(filename=full_path_file, extract_dir='.', format='zip')
    summa = 0
    path_folder = os.path.splitext(full_path_file)[0]
    for currentdir, dirs, files in os.walk(path_folder):
        for file in files:
            path_file = os.path.join(currentdir, file)
            summa += os.path.getsize(path_file)
    print(f'Общий размер всех файлов: {summa} Байт')  # в условии задачи не сказано о переводе в Мб и тд


if __name__ == "__main__":
    search_size_files()
