from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
]
