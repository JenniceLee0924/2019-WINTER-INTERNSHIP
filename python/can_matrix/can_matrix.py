#convert xlsx to csv
import csv
from collections import defaultdict
import xlrd
from collections import deque

def excel_to_csv():
    wb = xlrd.open_workbook('can_matrix_icm.xlsx')
    sh = wb.sheet_by_name('Matrix')
    can_matrix_csv = open('can_matrix_csv.csv','w')
    wr = csv.writer(can_matrix_csv,quoting=csv.QUOTE_ALL)

    for row in range(sh.nrows):
        wr.writerow(sh.row_values(row))

    can_matrix_csv.close()
#creating csv file
excel_to_csv()

file = 'can_matrix_csv.csv'

def convert_to_dic(file):
    #creating empty dictionary
    columns = defaultdict(list)
    #Going through each items of the rows
    with open(file, mode='r') as infile:
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
    return dic4

#!/usr/bin/env python

#convert int into hex
def int_hex(n):
    hex = '{n:x}'.format(n=n)
    if len(hex) & 1:
        hex = '0' + hex
    return hex

# convert signal info into can data
def makeCanData(Signal):
    dic = convert_to_dic(file)
    values = dic[Signal]
    bit = values[0]
    size = values[1]
    id = values[2]
    hex = int_hex(2**int(bit))
    hex = hex + '0x0'
    deq = deque([0] * 18)
    for i in hex:
        deq.appendleft(i)
    return deq



print(makeCanData('PositionLampStatus '))
print(int_hex(128))