# pip install numpy
import numpy as np


def main():
    try:
        data = [i.strip() for i in open('3_system.txt')]
        if len(data) == 0:
            print('файл пустой')
            return
        else:
            arr = np.loadtxt('3_system.txt', encoding='utf-8')
    except ValueError:
        print('возможно, в файле не числа или кол-во неизвестных != кол-во строк')
        return
    except FileNotFoundError:
        print('нет файла')
        return

    if arr.ndim == 1:  # если это линейное уравнение
        if len(arr) != 2:
            print('линейное уравнение не вида ax = b')
        elif arr[0] == 0 and arr[1] == 0:
            print('беск много решений')
        elif arr[0] == 0 and arr[1] != 0:
            print('нет решений')
        else:
            print(arr[1] / arr[0])
        return

    right = arr[:, -1]
    arr = arr[:, 0:-1]

    try:
        solution = np.linalg.solve(arr, right)
    except np.linalg.LinAlgError as text:
        print(f'не удалось решение: {text}')
        return

    print(f'решение: {", ".join(map(str, solution))}')


if __name__ == "__main__":
    main()
