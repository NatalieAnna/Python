import openpyxl

excel_files = ["Dogs.xlsx","Locations.xlsx"]

values = []

for file in excel_files:
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook['Sheet1']
    cell_value = worksheet['A2'].value
    values.append(cell_value)
    print(cell_value)

print(values)


"""
Prints:

Border Collie
Forest
['Border Collie', 'Forest']

"""
