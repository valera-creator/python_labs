# pip install pandas
import pandas as pd


def main():
    try:
        df = pd.read_csv("data_tallest_buildings.csv")
    except FileNotFoundError:
        print('нет файла')
        return


if __name__ == "__main__":
    main()
