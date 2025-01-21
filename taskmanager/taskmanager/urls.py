from django.contrib import admin
from django.urls import path
from . import views  # импортируем views из текущего приложения

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # главная страница отображает index.html
    path('about-us/', views.about_us, name='about_us'),  # функция views.about_us должна быть определена
]
