import csv
# Create your views here.
# 이 파일은 csv파일을 통합하기 위해 만들어진 파일입니다.
list = []
def readCSV(name, word):
    with open(name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 0
        for row in spamreader:
            element = []
            if i == 0:
                i += 1
                continue
            element.append(row[5]) #업소명
            element.append(row[4]) #운영 상태 
            element.append(row[6]) #업소 주소
            element.append(row[7]) #전화 번호
            element.append(word)
            list.append(element)

def readAllCSV():
    readCSV('./csv/서울시 강남구 소독업소 관리 현황.csv', "강남구")
    readCSV('./csv/서울시 광진구 소독업소 관리 현황.csv', "광진구")
    readCSV('./csv/서울시 구로구 소독업소 관리 현황.csv', "구로구")
    readCSV('./csv/서울시 노원구 소독업소 관리 현황.csv', "노원구")
    readCSV('./csv/서울시 마포구 소독업소 관리 현황.csv', "마포구")
    readCSV('./csv/서울시 성동구 소독업소 관리 현황.csv', "성동구")
    readCSV('./csv/서울시 송파구 소독업소 관리 현황.csv', "송파구")
    readCSV('./csv/서울시 영등포구 소독업소 관리 현황.csv', "영등포구")
    readCSV('./csv/서울시 종로구 소독업소 관리 현황.csv', "종로구")
    readCSV('./csv/서울시 중랑구 소독업소 관리 현황.csv', "중랑구")

readAllCSV()

#print(list)

with open('./csv/서울시 소독업소 관리 현황.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['업소명', '운영상태코드', '주소', '전화번호', '지역'])
    for i in list:
        spamwriter.writerow(i)
    