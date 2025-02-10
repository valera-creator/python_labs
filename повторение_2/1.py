import datetime


def search_cnt_days():
    today = datetime.datetime.today()
    data = input("введите дату рождения в формате YYYY-MM-DD: ")

    try:
        birthday = datetime.datetime.strptime(data, "%Y-%m-%d")  # по символу "-" делает объект времени
    except ValueError:
        print('неверный ввод')
        return

    cnt_days = (today - birthday).days
    if cnt_days < 0:
        print('из будущего что ли?')
    else:
        print(f'кол-во дней: {cnt_days}')


if __name__ == "__main__":
    search_cnt_days()
