#convert xlsx to csv
import csv
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

#read csv file
with open('can_matrix_csv.csv') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        print(row)


