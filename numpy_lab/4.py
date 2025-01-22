# pip install numpy
import numpy as np


def main():
    try:
        # dtype - автоматически тип данных установить
        # names - чтобы потом обращаться data['price], например + первая строка читается как имена столбцов
        data = np.genfromtxt(fname='udemy_courses.csv', delimiter=',', dtype=None, encoding='utf-8', names=True)
    except FileNotFoundError:
        print('нет файла')
        return
    except IndexError:
        print('пустой файл или проблемы с разным кол-вом столбцов')
        return
    except ValueError as text:
        print(text)
        return

    try:
        res = np.mean(data['price'])
        print(f'средняя цена {res}')
    except RuntimeWarning:
        print('нет значений')
        return
    except Exception as text:
        print(text)
        return

    try:
        res = np.min(data['num_subscribers'])
        print(f'минимальное число подписчиков: {res}')
    except RuntimeWarning:
        print('нет значений')
        return
    except ValueError:
        print('нет значений')
        return
    except Exception as text:
        print(text)
        return

    try:
        res = np.max(data['content_duration'])
        print(f'максимальная продолжительность лекций: {res}')
    except RuntimeWarning:
        print('нет значений')
        return
    except ValueError:
        print('нет значений')
        return
    except Exception as text:
        print(text)
        return

    # индексация сохраняется, для level[0] соответствует counts[0] и тд
    levels, counts = np.unique(data['level'], return_counts=True)
    print(levels, counts)
    max_count = np.max(counts)
    print('уровень (уровни, если их много одинакового кол-ва), для которых создано максимальное кол-во курсов: ')
    for i in range(len(counts)):
        if counts[i] == max_count:
            print(levels[i])


if __name__ == "__main__":
    main()
