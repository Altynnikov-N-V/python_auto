from xlrd import open_workbook

workbook = open_workbook("tmp/For_tests_xls.xls")
print(workbook.nsheets)
print(workbook.sheet_names())
sheet = workbook.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)
print(sheet.cell_value(rowx=2, colx=5))

for rx in range(sheet.nrows):
    print(sheet.row(rx))
