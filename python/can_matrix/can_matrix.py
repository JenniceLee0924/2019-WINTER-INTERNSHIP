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
    #delete empty values in dictionary
def DelNoneKey(dictionary):
    for i in dictionary.copy():
        if not dictionary[i]:
            dictionary.pop(i)
    return dictionary
# parsing can signal
def ParseCanSignal():
    #creating empty dictionary
    columns = defaultdict(list)
    #Going through each items of the rows
    with open(file, mode='r') as infile:
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
    startbit_dic = DelNoneKey(dict(zip(signal_name,start_bit)))
    signalsize_dic = DelNoneKey(dict(zip(signal_name,signal_size)))
    msgid_dic = DelNoneKey(dict(zip(signal_name,msg_id)))
    value_dic= DelNoneKey(dict(zip(signal_name,value_des)))

    # combining values of the same key into dictionary
    dictionary = defaultdict(list)
    for d in (startbit_dic,signalsize_dic,msgid_dic,value_dic):
        for key,value in d.items():
            dictionary[key].append(value)

    return dictionary


#convert int into hex
def IntHex(n):
    integer = n
    hex = integer.to_bytes((((integer.bit_length() + 7) // 8)), "little").hex()
    return hex


# convert signal info into can data
def MakeCanData(signal,value):
    signal = dic[signal]
    bit = signal[0]
    size = signal[1]
    id = signal[2]
    values = signal[3]
    big_end = IntHex((2**int(bit))*value)
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