import csv
import os, glob

def readCSV(name):
    with open(name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        list = []
        for row in spamreader:
            element = []
            element.append(row[5]) #업소명
            element.append(row[4]) #운영 상태 
            element.append(row[6]) #업소 주소
            element.append(row[7]) #전화번호
            list.append(element)
    return list

data = os.listdir('./data/')
for file in data:
    if file.endswith(".csv"):
        #print(os.path.join("./data/", file))
        list = readCSV(os.path.join("./data/", file))
    break

