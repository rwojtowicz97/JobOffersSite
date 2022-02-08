from dataclasses import field
from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from jobOffers.models import JobOffer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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

class JobOfferCreateView(LoginRequiredMixin, CreateView):
    model = JobOffer
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class JobOfferUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = JobOffer
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        jobOffer = self.get_object()
        if self.request.user == jobOffer.creator:
            return True
        return False


class JobOfferDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = JobOffer
    success_url = '/'

    def test_func(self):
        jobOffer = self.get_object()
        if self.request.user == jobOffer.creator:
            return True
        return False
    


def about(request):
    return render(request, 'jobOffers/about.html', {'title': 'About'})