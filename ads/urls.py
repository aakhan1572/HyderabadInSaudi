from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ads, name='ads'),
    path('photo/', views.photo_carousel, name='photo_carousel'),
]