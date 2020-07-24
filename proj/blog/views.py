from django.shortcuts import render
from .models import readCSV
# Create your views here.
def post_list(request):
    posts = readCSV('./csv/강남구.csv')
    title = posts[0]
    posts_list = posts[1:]
    return render(request, 'index.html', {'posts':posts_list , 'title':title})
