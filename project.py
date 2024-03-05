import os
import csv


class PriceMachine():

    def __init__(self):
        self.data = []

    def load_prices(self, folder_path):
        for file in os.listdir(folder_path):
            if 'price' in file:
                with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        self.data.append(row)

    def _search_product_price_weight(self, headers):
        name_col = None
        price_col = None
        weight_col = None
        for idx, header in enumerate(headers):
            if header.lower() in ['название', 'продукт', 'товар', 'наименование']:
                name_col = idx
            elif header.lower() in ['цена', 'розница']:
                price_col = idx
            elif header.lower() in ['вес', 'масса', 'фасовка']:
                weight_col = idx
        return name_col, price_col, weight_col

    def export_to_html(self, output_file_path=r'C:\Users\Denis\PycharmProjects\pythonProject2\output.html'):
        if self.data:
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write('''
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Позиции продуктов</title>
                </head>
                <body>
                    <table>
                        <tr>
                            <th>Номер</th>
                            <th>Название</th>
                            <th>Цена</th>
                            <th>Фасовка</th>
                            <th>Файл</th>
                            <th>Цена за кг.</th>
                        </tr>
                ''')
                for idx, row in enumerate(self.data, start=1):
                    file.write(
                        f"<tr><td>{idx}</td><td>{row.get('название', '')}</td><td>{row.get('цена', '')}</td><td>{row.get('вес', '')}</td><td>{row.get('файл', '')}</td><td>{float(row.get('цена', 0)) / float(row.get('вес', 1)):.1f}</td></tr>")
                file.write('''
                    </table>
                </body>
                </html>
                ''')
            print(f"HTML файл успешно создан: {output_file_path}")
        else:
            print("Нет данных для сохранения в HTML файл.")

    def find_text(self, text):
        results = []
        for row in self.data:
            for key, value in row.items():
                if 'название' in key.lower() and text.lower() in value.lower():
                    results.append(row)

        if results:
            print("Результаты поиска:")
            for idx, result in enumerate(results, start=1):
                print(
                    f"Название: {result.get('название', '')}, Цена: {result.get('цена', '')}, Вес: {result.get('вес', '')}, Файл: {result.get('файл', '')}")
        else:
            print("Нет результатов по вашему запросу.")

        return results


pm = PriceMachine()
folder_path = r'C:\Users\Denis\PycharmProjects\pythonProject2'

pm.load_prices(folder_path)
print('Данные успешно загружены.')

while True:
    user_input = input("Введите фрагмент наименования товара для поиска (или 'exit' для выхода): ")
    if user_input.lower() == 'exit':
        print("Работа завершена.")
        break

    search_results = pm.find_text(user_input)

    if search_results:
        print("№   наименование               цена вес   файл   цена за кг.")
        for idx, result in enumerate(search_results, start=1):
            print(
                f"{idx:<3} {result.get('название', ''):<30} {result.get('цена', ''):<5} {result.get('вес', ''):<4} {result.get('файл', ''):<10} {float(result.get('цена', 0)) / float(result.get('вес', 1)):<6.1f}")
    else:
        print("Нет результатов по вашему запросу.")

output_file_path = r'C:\Users\Denis\PycharmProjects\pythonProject2\output.html'
pm.export_to_html(output_file_path)
