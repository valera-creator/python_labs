# pip install pandas
import pandas as pd


def search_high_low_build(df):
    sorted_height_df = df.sort_values(by='height_m', ascending=[False])
    print('Самые высокие здания:')
    print(sorted_height_df[['name', 'height_m']].head(5))
    print('\nСамый низкие здания:')
    print(sorted_height_df[['name', 'height_m']].tail(5))


def search_heights(df):
    print(f'\nМинимальная высота здания: {df["height_m"].min()}')
    print(f'Максимальная высота здания: {df["height_m"].max()}')
    print(f'Средняя высота здания: {df["height_m"].mean()}')
    print(f'Медаинная высота здания: {df["height_m"].median()}')


def search_count_country(df):
    cnt_country = df["country"].nunique()
    print(f'\nКоличество уникальных стран, упомянутых в файле: {cnt_country}')


def search_old_new_build(df):
    old_year = df['year_built'].min()
    new_year = df['year_built'].max()

    old_builds_df = df.loc[df['year_built'] == old_year][['name', 'year_built']]
    new_builds_df = df.loc[df['year_built'] == new_year][['name', 'year_built']]

    print(f'\nСамые старые здания:\n{old_builds_df}')
    print(f'\nСамые новые здания:\n{new_builds_df}')


def make_new_frame(df):
    try:
        floors = int(input('\nВведите кол-во этажей для поиска дома, которые выше этого кол-ва этажей: '))
    except ValueError:
        print('не число')
        quit()

    if floors < 0:
        print('отрицательное кол-во этажей?')
        quit()

    df['all_floors'] = df['floors_above'] + df['floors_below_ground']
    selection_floor_df = df[df['all_floors'] > floors]
    if len(selection_floor_df.index) == 0:
        print('нет таких домов')
    else:
        print(selection_floor_df[['name', 'all_floors']])


def search_name_by_year(df):
    try:
        year = int(input('\nВведите год, чтобы узнать, какие здания были построены в этом году: '))
    except ValueError:
        print('не число')
        quit()

    if year < 0:
        print('отрицательный год?')
        quit()

    selection_year_df = df[df['year_built'] == year]
    if len(selection_year_df.index) == 0:
        print('нет таких зданий')
    else:
        print(f'\nЗдания, построенные в {year} году:\n {selection_year_df[["name", "year_built"]]}')


def search_cnt_builds(df):
    country_search = input('\nВведите страну для поиска в ней зданий: ')
    selection_country_df = df[df['country'].str.lower() == country_search.lower()]
    print(f'Количество зданий из файла в стране {country_search} = {selection_country_df["name"].count()}')


def main():
    try:
        df = pd.read_csv("data_tallest_buildings.csv", delimiter=',')
    except FileNotFoundError:
        print('нет файла')
        return

    search_high_low_build(df)
    search_heights(df)
    search_count_country(df)
    search_old_new_build(df)
    make_new_frame(df)
    search_name_by_year(df)
    search_cnt_builds(df)


if __name__ == "__main__":
    main()
