from django.urls import path
from .views import JobOfferListView, JobOfferDetailView, JobOfferCreateView, JobOfferUpdateView, JobOfferDeleteView
from . import views

app_name = 'jobOffers'

urlpatterns = [
    path('', JobOfferListView.as_view(), name='jobOffers-home'),
    path('jobOffers/<int:pk>/', JobOfferDetailView.as_view(), name ='jobOffers-detail'),
    path('jobOffers/new/', JobOfferCreateView.as_view(), name ='jobOffers-create'),
    path('jobOffers/<int:pk>/update/', JobOfferUpdateView.as_view(), name ='jobOffers-update'),
    path('jobOffers/<int:pk>/delete/', JobOfferDeleteView.as_view(), name ='jobOffers-delete'),
    path('about/', views.about, name='jobOffers-about'),
]