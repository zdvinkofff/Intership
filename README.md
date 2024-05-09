Практическое задание "Анализатор прайс-листов."
Техническая документация:

Описание программы:

Данная программа представляет собой реализацию класса PriceMachine, который предназначен для работы с базой данных цен на товары.
Класс PriceMachine загружает данные из CSV-файлов, расположенных в указанной папке, и предоставляет методы для поиска, сортировки и экспорта этих данных.
Методы класса PriceMachine:

__init__(self): Инициализирует объект PriceMachine и создает пустой список data для хранения загруженных данных.
load_prices(self, folder_path): Загружает данные из всех CSV-файлов, находящихся в указанной папке. Используется словарь key_mapping для поиска и сопоставления полей "название", "цена" и "вес" в CSV-файлах.
export_to_console(self): Выводит на консоль список всех загруженных товаров с их названием, ценой, весом и названием файла.
search_product(self, search_query): Выполняет поиск товаров, в названии которых содержится указанный поисковый запрос. Возвращает отсортированный список найденных товаров по соотношению цены и веса.
export_to_html(self, output_file_path=r'C:\Users\Denis\PycharmProjects\pythonProject2\output.html'): Экспортирует список всех загруженных товаров в HTML-файл с таблицей, отсортированной по соотношению цены и веса.
find_text(self, text): Выполняет поиск товаров, в названии которых содержится указанный текст. Возвращает отсортированный список найденных товаров по соотношению цены и веса.

Использование программы:
Создается объект PriceMachine.
Вызывается метод load_prices() для загрузки данных из CSV-файлов, расположенных в указанной папке.
Запускается бесконечный цикл, в котором пользователя просят ввести фрагмент наименования товара для поиска.
Если пользователь вводит "exit", программа завершает работу и вызывает метод export_to_html() для экспорта данных в HTML-файл.
Если пользователь вводит какой-либо текст, программа вызывает метод search_product() для поиска и вывода информации о соответствующих товарах.
Если ошибка при выполнении программы, выводится сообщение об ошибке.

Общая структура программы:
Импорт необходимых библиотек (os, csv).
Определение класса PriceMachine.
Создание объекта PriceMachine.
Загрузка данных из CSV-файлов.
Запуск цикла поиска товаров.
Экспорт данных в HTML-файл при завершении работы.
Обработка исключений.
Данная программа предоставляет возможность загружать, искать и экспортировать данные о товарах и их ценах из CSV-файлов.
