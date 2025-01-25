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

    fig.show()


def display_cnt_subscribers(df):
    is_paid = df[df['is_paid']]
    not_is_paid = df[~df['is_paid']]

    max_sub_paid = is_paid['num_subscribers'].max()
    min_sub_paid = is_paid['num_subscribers'].min()
    mean_sub_paid = is_paid['num_subscribers'].mean()

    max_sub_not_paid = not_is_paid['num_subscribers'].max()
    min_sub_not_paid = not_is_paid['num_subscribers'].min()
    mean_sub_not_paid = not_is_paid['num_subscribers'].mean()

    new_df = pd.DataFrame(
        {
            'Тип курса': ['Платные', 'Бесплатные'],
            'Максимальное кол-во подписчиков': [max_sub_paid, max_sub_not_paid],
            'Среднее кол-во подписчиков': [mean_sub_paid, mean_sub_not_paid],
            'Минимальное кол-во подписчиков': [min_sub_paid, min_sub_not_paid]
        }
    )

    # подписи и преобразования метрик
    new_df_melted = new_df.melt(id_vars='Тип курса', var_name='легенда', value_name='Количество подписчиков')

    # построение
    fig = px.bar(
        new_df_melted,
        x='Тип курса',
        y='Количество подписчиков',
        color='легенда',  # максимальное, среднее, минимальное
        barmode='group',  # Группировка столбцов
        title='Сравнение платных и бесплатных курсов по количеству подписчиков',
        text_auto=True  # Автоматическое отображение значений на столбцах
    )

    fig.show()


def main():
    try:
        df = pd.read_csv('udemy_courses_extended.csv', delimiter=',')
    except FileNotFoundError:
        print('нет файла')
        return

    display_cnt_courses(df)
    display_cnt_subscribers(df)


if __name__ == "__main__":
    main()
