from django.urls import path
from . import views

app_name = 'jobOffers'

urlpatterns = [
    path('', views.home, name='jobOffers-home'),
    path('about/', views.about, name='jobOffers-about'),
]