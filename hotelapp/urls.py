
from django.contrib import admin
from django.urls import path
from hotelapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('about/', views.about),
    path('services/', views.services),
]
