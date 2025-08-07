from zipfile import ZipFile

with ZipFile("tmp/for_test_zip.zip") as zip_file:
    print(zip_file.namelist())
    text = zip_file.read('for_test_zip')
    print(text)
    zip_file.extract('for_test_zip', path="tmp")
