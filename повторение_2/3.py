def get_data():
    path = input('путь: ')
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            data = [i.split() for i in file]
    except FileNotFoundError:
        print('нет тут файла, другой путь надо было')
        quit()

    try:
        data = list(map(lambda x: [x[0], int(x[1])], data))
    except ValueError:
        print('не число')
        quit()
    except IndexError:
        print('некорректное содержание файла')
        quit()

    if not data:
        quit()

    return data


def get_n():
    try:
        n = int(input('\nВведите число: '))
        return n
    except ValueError:
        print('не число')
        quit()


def main():
    data = get_data()

    data = sorted(data, key=lambda x: x[0])  # сортировка по имени
    print('Сортировка по имени:')
    for elem in data:
        print(f'{elem[0]} {elem[1]}')

    data = sorted(data, key=lambda x: x[1], reverse=True)  # сортировка по баллам
    print('\nСортировка по баллам:')
    for elem in data:
        print(f'{elem[0]} {elem[1]}')

    n = get_n()

    data = list(filter(lambda x: x[1] > n, data))
    with open('res.txt', mode='w', encoding='utf-8') as file:  # запись в файл
        for elem in data:
            file.write(f'{elem[0]}\n')


if __name__ == "__main__":
    main()
