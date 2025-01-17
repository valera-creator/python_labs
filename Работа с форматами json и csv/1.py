import json


def print_bird(data):
    print('данные о птицах:')
    try:
        res = list(filter(lambda x: x['animal_type'] == 'Bird', data['animals']))
    except KeyError:
        print('нет такого ключа')
        return
    for elem in res:
        print(elem)


def search_diurnal(data):
    try:
        res = len(list(filter(lambda x: x['active_time'] == 'Diurnal', data['animals'])))
    except KeyError:
        print('нет такого ключа')
        return
    print(f"\nкол-во дневных животных: {res}\n")


def search_min_weight(data):
    try:
        res = min(data['animals'], key=lambda x: float(x['weight_min']))['name']
    except KeyError:
        print('нет такого ключа')
        return
    except ValueError:
        print('вес - не число')
        return
    print(f"животное с наименьшим весом: {res}")


def main():
    try:
        with open('animals.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('нет файла')
        return
    except json.decoder.JSONDecodeError:
        print('некорректное содержнание файла')
        return

    print_bird(data)
    search_diurnal(data)
    search_min_weight(data)


if __name__ == "__main__":
    main()
