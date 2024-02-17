import os
import json


class PriceMachine():
    
    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0
    
    def load_prices(self, file_path='C:\Users\Denis\PycharmProjects\Practice Analizer price-lists'):
                for file_name in os.listdir(file_path):
                    if "price" in file_name:
                        with open(os.path.join(file_path, file_name), 'r') as file:
                            csv_reader = csv.DictReader(file, delimiter=';')
                            for row in csv_reader:
                                self.data.append(row)

    def export_to_html(self, file_path='output.html'):
        with open(output_file, 'w') as file:
            file.write('<html><body><table border="1">')
            file.write('<tr><th>№</th><th>Наименование</th><th>цена</th><th>вес</th><th>файл</th><th>цена за кг.</th></tr>')
            for idx, item in enumerate(self.data, 1):
                file.write(
                    f'<tr><td>{idx}</td><td>{item.get("название", "")}</td><td>{item.get("цена", "")}'
                    f'</td><td>{item.get("вес", "")}</td><td>{item.get("файл", "")}'
                    f'</td><td>{float(item.get("цена", 0)) / float(item.get("вес", 1))}</td></tr>')
            file.write('</table></body></html>')
    
    def find_text(self, text):
        result = []
        for item in self.data:
            if any(text.lower() in value.lower() for key, value in item.items() if
                   key in ["название", "продукт", "товар", "наименование"]):
                result.append(item)
        return sorted(result, key=lambda x: float(x.get("цена", 0)) / float(x.get("вес", 1)))
    
pm = PriceMachine()
print(pm.load_prices("C:\Users\Denis\PycharmProjects\Practice Analizer price-lists"))

while True:
    search_text = input("Введите текст для поиска (для выхода введите 'exit'): ")
    if search_text.lower() == 'exit':
        print("Работа завершена.")
        break

    found_items = analyzer.find_text(search_text)
    for idx, item in enumerate(found_items, 1):
        print(f"{idx} {item.get('название', '')} {item.get('цена', '')} {item.get('вес', '')} {item.get('файл', '')}  "
              f" {float(item.get('цена', 0)) / float(item.get('вес', 1))}")
print('the end')
print(pm.export_to_html("C:\Users\Denis\PycharmProjects\Practice Analizer price-lists"))
