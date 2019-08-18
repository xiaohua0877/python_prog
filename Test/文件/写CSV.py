import csv
import os
import time

def writecsv(path,data):
    with open(path, "w") as f:
        writer = csv.writer(f)
        for rowData in data:
            print("rowData=", rowData)
            writer.writerow(rowData)

def readcev(path):
    infolist = []
    with open(path, "r") as f:
        allFile = csv.reader(f)
        for row in allFile:
            infolist.append(row)
    return infolist

b = os.path.exists("E:\\testFile\\17")
if b:
    print("File Exist!")
else:
    os.mkdir("E:\\testFile\\17")

path = r"E:\\testFile\\17\\000002.csv"
#path = r"E:\\Python\\py17\\automatictext\\000001.csv"
writecsv(path, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print('2. 读文件- - - - - - - - - ')
info = readcev(path)
print(info)