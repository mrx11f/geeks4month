from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Главная страница")

def contacts_view(request):
    return HttpResponse("0777 235 246")

def about_view(request):
    return HttpResponse("Добро пожаловать на наш сайт!")