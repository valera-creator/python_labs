import math


def make_table():
    try:
        n = int(input('введите число: '))
    except ValueError:
        print('не число')
        return

    if n < 1:
        print('число меньше 1')
        return

    print('\t' + '\t'.join([str(i) for i in range(1, n + 1)]))

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == 1:
                print(i, end='\t')

            if math.gcd(i, j) == 1:
                print('X', end='\t')
            else:
                print('О', end='\t')
        print()


if __name__ == "__main__":
    make_table()
