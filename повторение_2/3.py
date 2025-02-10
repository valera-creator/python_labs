def main():
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
        return

    data = sorted(data, key=lambda x: x[0])  # сортировка по имени
    print('Сортировка по имени:')
    for elem in data:
        print(f'{elem[0]} {elem[1]}')

    data = sorted(data, key=lambda x: x[1], reverse=True)  # сортировка по баллам
    print('\nСортировка по баллам:')
    for elem in data:
        print(f'{elem[0]} {elem[1]}')

    try:
        n = int(input('\nВведите число: '))
    except ValueError:
        print('не число')
        quit()

    with open('res.txt', mode='w', encoding='utf-8') as file:  # запись в файл
        for elem in data:
            if elem[1] > n:
                file.write(f'{elem[0]}\n')


if __name__ == "__main__":
    main()
