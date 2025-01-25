# pip install plotly
import plotly.express as px
import pandas as pd


def main():
    try:
        df = pd.read_csv('data_country.csv', delimiter=',')
    except FileNotFoundError:
        print('нет файла')
        return

    fig = px.imshow(
        df,
        text_auto=True,  # значение в ячейках
        aspect="auto",  # автоматическое подстроение соотношения сторон
        title='Тепловая карта по странам',
        labels=dict(x="Параметры", y="Страны", color="Значение"),  # подписи
        y=df['country'],

    )
    fig.show()


if __name__ == "__main__":
    main()
