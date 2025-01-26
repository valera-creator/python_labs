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


def display_courses_by_level(df):
    # Замена True и False на слова
    df['is_paid'] = df['is_paid'].replace({True: 'Платный', False: 'Бесплатный'})

    # кол-во строк сгруппированных
    grouped_size = df.groupby(['level', 'is_paid']).size()

    # превращение в фрейм, раскладывание на столбцы
    new_df = grouped_size.unstack()

    # замена NaN на 0 (если NaN, будем считать, что таких курсов 0)
    new_df = new_df.fillna(0)

    # Преобразование индекса в столбец
    new_df = new_df.reset_index()

    # подписи и преобразования метрик
    # id_vars - снизу
    # var_name - там, где легенда диаграммы, подпись цветов
    # value_name - слева
    new_df_melted = new_df.melt(id_vars='level', var_name='Тип курса', value_name='Кол-во курсов')

    # построение
    fig = px.bar(
        new_df_melted,
        x='level',
        y='Кол-во курсов',
        color='Тип курса',
        barmode='group',  # Группировка столбцов
        title='Кол-во курсов на бесплатных и платных курсах на разных уровнях',
        text_auto=True  # Автоматическое отображение значений на столбцах
    )

    fig.update_traces(textposition='outside')
    fig.show()


def main():
    try:
        df = pd.read_csv('udemy_courses_extended.csv', delimiter=',')
    except FileNotFoundError:
        print('нет файла')
        return

    display_cnt_courses(df)
    display_cnt_subscribers(df)
    display_courses_by_level(df)


if __name__ == "__main__":
    main()
