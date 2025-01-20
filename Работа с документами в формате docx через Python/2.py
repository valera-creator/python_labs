# pip install docxtpl
from docxtpl import DocxTemplate
import csv


def main():
    doc = DocxTemplate("template.docx")
    try:
        with open('data_marathon.csv') as csvfile:
            data = list(csv.reader(csvfile, delimiter=',', quotechar='"'))

    except FileNotFoundError:
        print('нет файла')
        return

    if not data:
        print('пустой файл')
        return

    data = sorted(data, key=lambda x: x[0])

    group_year = {}
    for elem in data:
        if elem[0] not in group_year:
            group_year[elem[0]] = []
        group_year[elem[0]].append(elem)

    for year, marathons in group_year.items():
        context = {
            "year": year,
            "marathons": [
                {
                    "city": marathon[5],
                    "name": marathon[1],
                    "gender": marathon[2],
                    "time": marathon[4],
                }
                for marathon in marathons
            ]
        }
        doc.render(context)
        doc.add_page_break()

        # Сохранение документа
    doc.save('res.docx')


if __name__ == "__main__":
    main()
