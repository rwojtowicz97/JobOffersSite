from django.urls import path
from .views import JobOfferListView, JobOfferDetailView, JobOfferCreateView
from . import views

app_name = 'jobOffers'

urlpatterns = [
    path('', JobOfferListView.as_view(), name='jobOffers-home'),
    path('jobOffers/<int:pk>/', JobOfferDetailView.as_view(), name ='jobOffers-detail'),
    path('jobOffers/new/', JobOfferCreateView.as_view(), name ='jobOffers-create'),
    path('about/', views.about, name='jobOffers-about'),
]