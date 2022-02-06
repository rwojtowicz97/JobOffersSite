from django.db import models
from django.contrib.auth.models import User

class JobOffer(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    finish_date = models.DateTimeField('date offer ends')

    def __str__(self):
        return self.title or ''


    
