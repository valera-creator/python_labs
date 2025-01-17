import csv


def get_num(text):
    try:
        return int(input(text))
    except ValueError:
        print('не число')
        quit()


def write_range(data):
    left = get_num('Левая граница: ')
    right = get_num('Правая граница: ')

    if left > right:
        print('левая граница больше правой')
        quit()

    with open('res1.csv', mode='w', newline='', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        res = list(filter(lambda x: left <= float(x[2]) <= right, data[1:]))
        for elem in res:
            writer.writerow(elem)


def write_sorted_inflation(data):
    data_sorted = sorted(data[1:], key=lambda x: float(x[3]))
    with open('res2.csv', mode='w', newline='', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for elem in data_sorted:
            writer.writerow(elem)


def main():
    try:
        with open('countries.csv') as csvfile:
            data = list(csv.reader(csvfile, delimiter=',', quotechar='"'))

    except FileNotFoundError:
        print('нет файла')
        return

    if not data:
        print('пустой файл')
        return

    write_range(data)
    write_sorted_inflation(data)


if __name__ == "__main__":
    main()
