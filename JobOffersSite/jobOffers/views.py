from dataclasses import field
from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from jobOffers.models import JobOffer


def home(request):
    context = {
        'offers': JobOffer.objects.all
    }
    return render(request, 'jobOffers/home.html', context)


class JobOfferListView(ListView):
    model = JobOffer
    template_name = 'jobOffers/home.html'
    context_object_name = 'offers'
    ordering = ['-pub_date']

class JobOfferDetailView(DetailView):
    model = JobOffer

class JobOfferCreateView(CreateView):
    model = JobOffer
    fields = ['title', 'description']


def about(request):
    return render(request, 'jobOffers/about.html', {'title': 'About'})