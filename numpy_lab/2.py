# pip install numpy
import numpy as np


def main():
    try:
        n = int(input('введите n: '))
    except ValueError:
        print('не число')
        return

    if n < 0:
        print('отрицательный размер матрицы не может быть')
        return

    if n == 0:
        print('размер матрицы 0, нечего сравнивать')
        return

    matrix_a = np.random.randint(0, 101, size=(n, n))
    print('matrix_a:')
    print(matrix_a)
    print()

    cur_min = matrix_a[:, 0].sum()  # по первому столбцу

    for i in range(n):
        summa = matrix_a[:, i].sum()
        if summa < cur_min:
            cur_min = summa

    for i in range(n):  # если таких столбцов несколько
        summa = matrix_a[:, i].sum()
        if summa == cur_min:
            print(f'в {i + 1}-ом столбце сумма минимальна')


if __name__ == "__main__":
    main()
