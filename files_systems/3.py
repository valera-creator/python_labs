import shutil
import os


def search_size_files():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    full_path_src = "D://projects/laba_python/files_systems/test_3"
    # full_path_src = input('Введите путь src: ')

    full_path_dst = "D://projects/laba_python/files_systems/res_3"
    # full_path_dst = input('Введите путь dst: ')

    for currentdir, dirs, files in os.walk(full_path_src):
        for file in files:
            path_file = os.path.join(currentdir, file)
            if os.path.splitext(path_file)[-1] in extensions:
                shutil.move(path_file, full_path_dst)


if __name__ == "__main__":
    search_size_files()
