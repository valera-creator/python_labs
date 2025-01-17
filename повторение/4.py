def main():
    path = input('путь: ')
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            data = ''.join([''.join(i.lower().split()) for i in file])
    except FileNotFoundError:
        print('нет тут файла, другой путь надо было')
        return

    with open('res.txt', mode='w', encoding='utf-8') as file:
        for elem in set(data):
            file.write(f'{elem}: {data.count(elem)}\n')


if __name__ == "__main__":
    main()
