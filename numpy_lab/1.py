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
    matrix_b = np.random.randint(0, 101, size=(n, n))

    print('matrix_a:')
    print(matrix_a)
    print()

    print('matrix_b:')
    print(matrix_b)
    print()

    print('сравнение равенства матриц')
    matrix_equal = matrix_a == matrix_b
    print(matrix_equal)
    print()

    print('сравнение a < b')
    matrix_less = matrix_a < matrix_b
    print(matrix_less)
    print()

    print('сравнение a > b')
    matrix_more = matrix_a > matrix_b
    print(matrix_more)
    print()


if __name__ == "__main__":
    main()
