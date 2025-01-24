# pip install pandas
import pandas as pd


def search_high_low_build(df):
    sorted_height = df.sort_values(by='height_m', ascending=[False])
    print('самые высокие здания:')
    print(sorted_height[['name', 'height_m']].head(5))
    print('\nсамый низкие здания:')
    print(sorted_height[['name', 'height_m']].tail(5))


def search_heights(df):
    print(f'\nМинимальная высота здания: {df["height_m"].min()}')
    print(f'Максимальная высота здания: {df["height_m"].max()}')
    print(f'Средняя высота здания: {df["height_m"].mean()}')
    print(f'Медаинная высота здания: {df["height_m"].median()}')


def search_count_country(df):
    cnt_country = df["country"].nunique()
    print(f'\nколичество уникальных стран, упомянутых в файле: {cnt_country}')


def search_old_new_build(df):
    old_year = df['year_built'].min()
    new_year = df['year_built'].max()

    old_builds = df.loc[df['year_built'] == old_year][['name', 'year_built']]
    new_builds = df.loc[df['year_built'] == new_year][['name', 'year_built']]

    print(f'\nСамые старые здания:\n{old_builds}')
    print(f'\nСамые новые здания:\n{new_builds}')


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


if __name__ == "__main__":
    main()
