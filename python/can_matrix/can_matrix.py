import re
import sys
import csv
from collections import defaultdict
import xlrd
from collections import deque
from textwrap import wrap


CAN_MATRIX_EXCEL_FILE_NAME  = "can_matrix_icm.xlsx"
CAN_MATRIX_CSV_FILE_NAME  = "can_matrix_csv.csv"


#converting csv file
def ConvertExcelToCSV():
    wb = xlrd.open_workbook(CAN_MATRIX_EXCEL_FILE_NAME)
    sh = wb.sheet_by_name('Matrix')
    can_matrix_csv = open(CAN_MATRIX_CSV_FILE_NAME, mode='w', encoding='utf8')
    wr = csv.writer(can_matrix_csv,quoting=csv.QUOTE_ALL)

    for row in range(sh.nrows):
        wr.writerow(sh.row_values(row))

    can_matrix_csv.close()
    return True

# parsing can signal
def ParseCanSignal():
    #creating empty dictionary
    columns = defaultdict(list)
    #Going through each items of the rows
    with open(CAN_MATRIX_CSV_FILE_NAME, mode='r', encoding='utf8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            for (k,v) in row.items():
                columns[k].append(v)

    #Creating columns
    signal_name = columns['Signal Name']
    start_bit = columns['Start Bit\n(LSB)']
    signal_size = columns['Signal Size']
    msg_id = columns['Msg ID']
    value_des = columns['Value_Description']

    #Creating dictionary with Signal_Name as key
    startbit_dic = dict(zip(signal_name,start_bit))
    signalsize_dic = dict(zip(signal_name,signal_size))
    msgid_dic = dict(zip(signal_name,msg_id))
    temp_value_dic= dict(zip(signal_name,value_des))
    sort_temp_value_dic = sorted(temp_value_dic.items())

    #Creating list to append splited value description
    words = []
    #Split value descption by : and space
    for i in range(len(sort_temp_value_dic)):
        for j in range(1):
            words.append(re.split('[:,"\n"]', sort_temp_value_dic[i][1]))
    valuedes_dic = dict(zip(signal_name,words))

    # combining values of the same key into dictionary
    dictionary = defaultdict(list)
    for d in (startbit_dic,signalsize_dic,msgid_dic,valuedes_dic):
        for key,value in d.items():
            dictionary[key].append(value)

    return dictionary


#convert int into hex
def IntHex(n):
    hex = '{n:x}'.format(n=n)
    if len(hex) & 1:
        hex = '0' + hex
    return hex


# convert signal info into can data
def MakeCanData(can_dictionary, signal_name):
    values = can_dictionary[signal_name]
    bit = values[0]
    size = values[1]
    id = values[2]
    little_end = IntHex(2**int(bit))
    little_end = wrap(little_end,2)
    big_end = list(reversed(little_end))
    big_end = ''.join(big_end)
    hex_list = [0]*16
    for i in range(len(big_end)):
        if big_end:
            hex_list[i] = big_end[i]
    can_data = ''.join(str(i) for i in hex_list)
    can_data = '0x' + can_data
    return can_data


def main():
    if ( not ConvertExcelToCSV() ):
        print( "ConvertExcelToCSV() error\n" )
        return False

    can_dictionary = ParseCanSignal()
    if not can_dictionary:
        print( "ParseCanSignal() error\n" )
        return False

    print(MakeCanData( can_dictionary, 'LFDoorStatus' ))
    #1.for(name: Signal)
        #for(value: 2 ** signal size)
            #MakeCanData(name,value)

    #2. signal, value, can id, can data

    #3. if (value != datamodel(signal,can id,can data) ERROR

    return True

if __name__ == "__main__":
	if ( main() ):
		sys.exit( 0 )
	else:
		sys.exit( -1 )