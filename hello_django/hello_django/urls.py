from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about),
    path('home/', views.home),
    path('reverse/', views.reverse, name ='reversed'),
]
