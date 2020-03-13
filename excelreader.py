import xlrd
from datetime import *

data = xlrd.open_workbook('E:\\cfd\\cfd.xlsx')
sheet_name = "Sheet1"

table = data.sheets()[0]
table1 = data.sheet_by_name(sheet_name)

start_date = datetime.strptime('2018-06-11', '%Y-%m-%d')
print (table1.nrows)
print (table1.ncols)
print (table1.cell(4,4))



