import os
import csv

class PriceMachine():

    def __init__(self):
        self.data = []

    def load_prices(self, folder_path):
        key_mapping = {
            1: ['цена', 'товар', 'опт', 'масса'],
            2: ['наименование', 'опт', 'вес', 'цена'],
            3: ['название', 'вес', 'цена', 'опт'],
            4: ['продукт', 'розница', 'опт', 'фасовка']
        }

        for file in os.listdir(folder_path):
            if 'price' in file:
                with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        for key_set in key_mapping.values():
                            data = {}
                            for key in key_set:
                                data[key] = row.get(key, '')
                            self.data.append(data)

    def export_to_html(self, output_file_path=r'C:\Users\Denis\PycharmProjects\pythonProject2\output.html'):
        if self.data:
            valid_data = [row for row in self.data if row.get('цена') and row.get('вес')]
            unique_data = []
            item_names = set()
            for row in valid_data:
                item_name = row.get('название')
                if item_name not in item_names:
                    unique_data.append(row)
                    item_names.add(item_name)

            sorted_data = sorted(unique_data, key=lambda x: float(x.get('цена', 0)) / float(x.get('вес', 1)))

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
                            <th>№</th>
                            <th>Наименование</th>
                            <th>Цена</th>
                            <th>Вес</th>
                            <th>Файл</th>
                            <th>Цена за кг.</th>
                        </tr>
                ''')
                for idx, row in enumerate(sorted_data, start=1):
                    item_name = row.get('название', '')
                    price_per_kg = float(row.get('цена', 0)) / float(row.get('вес', 1))
                    file.write(
                        f"<tr><td>{idx}</td><td>{item_name}</td><td>{row.get('цена', '')}</td><td>{row.get('вес', '')}</td><td>{row.get('файл', '')}</td><td>{price_per_kg:.1f}</td></tr>"
                    )
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

try:
    pm.load_prices(folder_path)
    print('Данные успешно загружены.')

    while True:
        user_input = input("Введите фрагмент наименования товара для поиска (или 'exit' для выхода): ")
        if user_input.lower() == 'exit':
            print("Работа завершена.")
            break

        search_results = pm.find_text(user_input)
        search_results.sort(key=lambda x: float(x.get('цена', 0)) / float(x.get('вес', 1)))

        if search_results:
            print("№   Наименование                    Цена  Вес   Файл       Цена за кг.")
            for idx, result in enumerate(search_results, start=1):
                print(f"{idx:<3} {result.get('название', ''):<30} {result.get('цена', ''):<5} {result.get('вес', ''):<4} {result.get('файл', ''):<10} {float(result.get('цена', 0)) / float(result.get('вес', 1)):<6.1f}")
        else:
            print("Нет результатов по вашему запросу.")

    output_file_path = r'C:\Users\Denis\PycharmProjects\pythonProject2\output.html'
    pm.export_to_html(output_file_path)
except Exception as e:
    print(f"Произошла ошибка: {e}")
