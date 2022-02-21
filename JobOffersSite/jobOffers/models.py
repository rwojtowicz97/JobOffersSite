from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_prometheus.models import ExportModelOperationsMixin



class JobOffer(ExportModelOperationsMixin('joboffer'), models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    pub_date = models.DateTimeField(default=timezone.now)
    finish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title or ''
    
    
    def get_absolute_url(self):
        return reverse('jobOffers:jobOffers-detail', kwargs={'pk': self.pk})


    
