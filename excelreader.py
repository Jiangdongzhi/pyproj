import xlrd

data = xlrd.open_workbook('E:\\Dorian\\plant.xlsx')
sheet_name = "Machine"

table = data.sheets()[0]
table1 = data.sheet_by_name(sheet_name)

print (table1.nrows)

print (table1.cell(4,4))

