def search_ngramm():
    path = input('введите путь к файлу: ')
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            data = [i.strip() for i in file]
    except FileNotFoundError:
        print('нет файла')
        return

    data = ' '.join(data).split()

    try:
        n = int(input('введите натуральное число: '))
    except ValueError:
        print('не число')
        return

    if n < 1:
        print('число меньше 1')
        return

    if n > len(data):
        print('таких длинных n-грамм нет в файле')
        return

    for i in range(0, len(data) - n + 1):
        print(" ".join(data[i:i + n]))


if __name__ == "__main__":
    search_ngramm()
