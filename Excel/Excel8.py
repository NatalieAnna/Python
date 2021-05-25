# calculates human_years (col) from dog_years (col) and appends to spreadsheet

import openpyxl

file = 'Dogs.xlsx'
workbook = openpyxl.load_workbook(file)
worksheet = workbook['Sheet1']

for i in range(2,4):
    dog_years = worksheet.cell(row=i, column=5).value
    human_years_calc = dog_years + 15
    # human_years = worksheet.cell(row=i, column=6).value
    worksheet.cell(row=i, column=6).value = human_years_calc

workbook.save(file)
