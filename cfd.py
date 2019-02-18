import xlrd
from datetime import *

data = xlrd.open_workbook('E:\\cfd\\Book_test.xlsx')
sheet_name = "Test_Data"
date_format = '%Y/%m/%d'

table = data.sheets()[0]
sheet = data.sheet_by_name(sheet_name)

start_date = datetime.strptime('2018-02-03', '%Y-%m-%d')
print (sheet.nrows)
print (sheet.ncols)

a1 = sheet.cell_value(rowx=1, colx=3)
a1_as_datetime = datetime(*xlrd.xldate_as_tuple(a1, data.datemode))
print 'datetime: %s' % a1_as_datetime

print (a1_as_datetime.strftime( '%w' )) # 5 means Friday. 0 means Sunday

