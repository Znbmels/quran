from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return HttpResponse("Добро пожаловать на главную страницу!")


def index(request):
    return render(request, 'main/index.html')

def about_us(request):
    return render(request, 'about_us.html')



