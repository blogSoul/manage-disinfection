# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

import csv
import os, glob
from django.core.files.storage import FileSystemStorage

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    #게시판 확인용

def readCSV(name):
    with open(name, newline='', mode='r') as csvfile:
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