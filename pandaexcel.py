import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

filename = 'E:\\Dorian\\plant.xlsx'
sheetname = 'Machine'
df = pd.read_excel(filename, sheet_name = sheetname)

print ("column headings:")
print (df.columns)

for i in range(18,30):
    print (i)
