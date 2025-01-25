# pip install plotly
import plotly.express as px
import pandas as pd


def display_cnt_courses(df):
    data = df[['course_title', 'is_paid']]
    is_paid = data[data['is_paid']].shape[0]
    not_is_paid = data[~data['is_paid']].shape[0]

    counts_df = pd.DataFrame(
        {
            'Тип курса': ['Платные', 'Бесплатные'],
            'Количество курсов': [is_paid, not_is_paid]
        }
    )

    # Построение диаграммы
    fig = px.bar(
        counts_df,
        x='Тип курса',
        y='Количество курсов',
        title='Количество платных и бесплатных курсов на Udemy',
        text='Количество курсов'
    )

    # Настройка отображения текста над значениями диаграммы
    fig.update_traces(textposition='outside')

    # Показ диаграммы
    fig.show()


def main():
    try:
        df = pd.read_csv('udemy_courses_extended.csv', delimiter=',')
    except FileNotFoundError:
        print('нет файла')
        return

    display_cnt_courses(df)


if __name__ == "__main__":
    main()
