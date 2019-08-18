import csv


def readcev(path):
    infolist = []
    with open(path, "r") as f:
        allFile = csv.reader(f)
        for row in allFile:
            infolist.append(row)
    return infolist


path = r"E:\\Python\\py17\\automatictext\\PCB3.csv"
info = readcev(path)
