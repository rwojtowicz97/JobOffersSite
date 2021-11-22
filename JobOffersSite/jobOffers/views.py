from django.shortcuts import render
from django.http import HttpResponse

from jobOffers.models import JobOffer


offers = [
    {
        'company': 'TestA',
        'title': 'titleA',
        'description': 'description',
        'pub_date': '27-01-2021',
        'finish_date': '05-02-2021'
    },
    {
        'company': 'TestB',
        'title': 'titleB',
        'description': 'description',
        'pub_date': '11-04-2021',
        'finish_date': '18-04-2021'
    }
]


def home(request):
    context = {
        'offers': offers
    }
    return render(request, 'jobOffers/home.html', context)

def about(request):
    return render(request, 'jobOffers/about.html', {'title': 'About'})