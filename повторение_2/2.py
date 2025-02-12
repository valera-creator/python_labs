import math


def get_n():
    try:
        n = int(input('введите число: '))
    except ValueError:
        print('не число')
        quit()

    if n < 1:
        print('число меньше 1')
        quit()

    return n


def make_table():
    n = get_n()

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
