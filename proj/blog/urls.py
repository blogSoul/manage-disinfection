from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('gang/', views.gang_list, name='gang_list'),
    path('gwang/', views.gwang_list, name='gwang_list'),
    path('gu/', views.gu_list, name='gu_list'),
    path('no/', views.no_list, name='no_list'),
    path('ma/', views.ma_list, name='ma_list'),
    path('seong/', views.seong_list, name='seong_list'),
    path('song/', views.song_list, name='song_list'),
    path('yeong/', views.yeong_list, name='yeong_list'),
    path('jong/', views.jong_list, name='jong_list'),
    path('jung/', views.jung_list, name='jung_list'),
]