from django.shortcuts import render
from .models import CsvData
import csv
# Create your views here.
def readCSV(name, num):
    with open(name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        list = []
        for row in spamreader:
            '''
            CsvData.name = row[5] #업소명
            CsvData.iswork = row[4] #운영 상태 
            CsvData.address = row[6] #업소 주소
            CsvData.phone = row[7] #전화 번호
            '''
            model_instance = CsvData(name = row[5], iswork = row[4], address = row[6], phone = row[7], checkPlace = num)
            model_instance.save()

def readAllCSV():
    readCSV('./csv/서울시 강남구 소독업소 관리 현황.csv', 1)
    readCSV('./csv/서울시 광진구 소독업소 관리 현황.csv', 2)
    readCSV('./csv/서울시 구로구 소독업소 관리 현황.csv', 3)
    readCSV('./csv/서울시 노원구 소독업소 관리 현황.csv', 4)
    readCSV('./csv/서울시 마포구 소독업소 관리 현황.csv', 5)
    readCSV('./csv/서울시 성동구 소독업소 관리 현황.csv', 6)
    readCSV('./csv/서울시 송파구 소독업소 관리 현황.csv', 7)
    readCSV('./csv/서울시 영등포구 소독업소 관리 현황.csv', 8)
    readCSV('./csv/서울시 종로구 소독업소 관리 현황.csv', 9)
    readCSV('./csv/서울시 중랑구 소독업소 관리 현황.csv', 10)

if CsvData.objects.all == None:
    readAllCSV()
else:
    pass

def post_list(request):
    posts_list = CsvData.objects.all()[1:]
    title = CsvData.objects.all().first()
    return render(request, 'index.html', {'posts':posts_list, 'title':title})

def gang_list(request):
    posts_list = CsvData.objects.filter(checkPlace = 1)[1:]
    title = CsvData.objects.filter(checkPlace = 1).first()
    return render(request, 'blog/강남구.html', {'posts':posts_list, 'title':title})

def gwang_list(request):
    posts_list = CsvData.objects.filter(checkPlace = 2)[1:]
    title = CsvData.objects.filter(checkPlace = 2).first()
    return render(request, 'blog/광진구.html', {'posts':posts_list, 'title':title})

def gu_list(request):
    posts_list = CsvData.objects.filter(checkPlace = 3)[1:]
    title = CsvData.objects.filter(checkPlace = 3).first()
    return render(request, 'blog/구로구.html', {'posts':posts_list, 'title':title})

def no_list(request):
    posts_list = CsvData.objects.filter(checkPlace = 4)[1:]
    title = CsvData.objects.filter(checkPlace = 4).first()
    return render(request, 'blog/노원구.html', {'posts':posts_list, 'title':title})

def ma_list(request):
    posts_list = CsvData.objects.filter(checkPlace = 5)[1:]
    title = CsvData.objects.filter(checkPlace = 5).first()
    return render(request, 'blog/마포구.html', {'posts':posts_list, 'title':title})

def seong_list(request):
    posts_list = CsvData.objects.filter(checkPlace = 6)[1:]
    title = CsvData.objects.filter(checkPlace = 6).first()
    return render(request, 'blog/성동구.html', {'posts':posts_list, 'title':title})

def song_list(request):
    posts_list = CsvData.objects.filter(checkPlace = 7)[1:]
    title = CsvData.objects.filter(checkPlace = 7).first()
    return render(request, 'blog/송파구.html', {'posts':posts_list, 'title':title})

def yeong_list(request):
    posts_list = CsvData.objects.filter(checkPlace = 8)[1:]
    title = CsvData.objects.filter(checkPlace = 8).first()
    return render(request, 'blog/영등포구.html', {'posts':posts_list, 'title':title})

def jong_list(request):
    posts_list = CsvData.objects.filter(checkPlace = 9)[1:]
    title = CsvData.objects.filter(checkPlace = 9).first()
    return render(request, 'blog/종로구.html', {'posts':posts_list, 'title':title})

def jung_list(request):
    posts_list = CsvData.objects.filter(checkPlace = 10)[1:]
    title = CsvData.objects.filter(checkPlace = 10).first()
    return render(request, 'blog/중랑구.html', {'posts':posts_list, 'title':title})