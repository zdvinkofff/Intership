import os
import csv


class PriceMachine:

    def __init__(self):
        self.data = []

    def load_prices(self, file_path='C:/Users/Denis/PycharmProjects/pythonProject2', encoding='utf-8'):
        for file_name in os.listdir(file_path):
            if "price" in file_name:
                with open(os.path.join(file_path, file_name), 'r', encoding=encoding) as file:
                    csv_reader = csv.DictReader(file, delimiter=';')
                    for row in csv_reader:
                        self.data.append(row)

    def export_to_html(self, file_path='C:/Users/Denis/PycharmProjects/pythonProject2/output.html'):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('<html><body><table border="1">\n')
            file.write(
                '<tr><th>№</th><th>Наименование</th><th>цена</th><th>вес</th><th>файл</th><th>цена за кг.</th></tr>\n')
            for idx, item in enumerate(self.data, 1):
                file.write(f'<tr><td>{idx}</td><td>{item.get("Наименование", "")}</td>'
                           f'<td>{item.get("цена", "")}</td><td>{item.get("вес", "")}</td>'
                           f'<td>{item.get("файл", "")}</td><td>{float(item.get("цена", 0)) / float(item.get("вес", 1))}</td></tr>\n')
            file.write('</table></body></html>')

        print(f'Файл {file_path} успешно создан.')

    def find_text(self, text):
        result = []
        for item in self.data:
            if any(text.lower() in value.lower() for key, value in item.items() if
                   key in ["название", "продукт", "товар", "наименование"]):
                result.append(item)
        return sorted(result, key=lambda x: float(x.get("цена", 0)) / float(x.get("вес", 1)))



pm = PriceMachine()


pm.load_prices(r"C:/Users/Denis/PycharmProjects/pythonProject2", encoding='utf-8')


pm.export_to_html(r"C:/Users/Denis/PycharmProjects/pythonProject2/output.html")
