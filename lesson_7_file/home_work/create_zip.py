import os
import zipfile

archive_name = "hw_archive.zip"
files_to_add = [
    'For_tests_hw_csv.csv',
    'For_tests_hw_xls.xls',
    'Tests_hw.pdf'
]

with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_add:
        if os.path.exists(file):
            zipf.write(file)      
            print(f'Добавлен файл: {file}')
        else:
            print(f"Файл не найден: {file}")

print("\nСодержимое архива:")
with zipfile.ZipFile(archive_name, 'r') as zipf:
    for file_info in zipf.infolist():
        print(f"- {file_info.filename} ({file_info.file_size} байт)")

print(f"\nАрхив успешно создан: {os.path.abspath(archive_name)}")

with zipfile.ZipFile(archive_name, 'r') as zip_ref:
    file_list = zip_ref.namelist()
    print(f"Файлы в архиве: {file_list}\n")
    for file_name in file_list:
        print(f"Анализ файла: {file_name}")
        if file_name.endswith('.csv'):
            print("Тип: CSV файл")
            with zip_ref.open(file_name) as file:
                first_line = file.readline().decode('utf-8').strip()
                print(f"Заголовки столбцов: {first_line}")
        elif file_name.endswith('.pdf'):
            print("Тип: PDF документ")
            with zip_ref.open(file_name) as file:
                magic_number = file.read(4)
                print(f"PDF сигнатура: {magic_number}")
        else:
            print("Тип: Неизвестный/другой формат")
            with zip_ref.open(file_name) as file:
                size = len(file.read())
                print(f"Размер файла: {size} байт")

        print("-" * 50)




