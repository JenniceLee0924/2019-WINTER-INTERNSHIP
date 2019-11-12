#convert xlsx to csv
import csv
from collections import defaultdict
import xlrd

def excel_to_csv():
    wb = xlrd.open_workbook('can_matrix_icm.xlsx')
    sh = wb.sheet_by_name('Matrix')
    can_matrix_csv = open('can_matrix_csv.csv','w')
    wr = csv.writer(can_matrix_csv,quoting=csv.QUOTE_ALL)

    for row in range(sh.nrows):
        wr.writerow(sh.row_values(row))

    can_matrix_csv.close()

excel_to_csv()

#creating empty dictionary
columns = defaultdict(list)
#Going through each items of the rows
with open('can_matrix_csv.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)
#Creating columns
Signal_Name = columns['Signal Name']
Start_Bit = columns['Start Bit\n(LSB)']
Signal_Size = columns['Signal Size']
Msg_ID = columns['Msg ID']


#Creating dictionary with Signal_Name as key
dic1 = dict(zip(Signal_Name,Start_Bit))
dic2 = dict(zip(Signal_Name,Signal_Size))
dic3 = dict(zip(Signal_Name,Msg_ID))

dic4 = defaultdict(list)
#combining values of the same key
for d in (dic1,dic2,dic3):
    for key,value in d.items():
        dic4[key].append(value)
print(dic4)
