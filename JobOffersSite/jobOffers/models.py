from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    creation_date = models.DateTimeField('creation date')
    mail = models.CharField(max_length=50)
    official_site = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=100)


class JobOffer(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    finish_date = models.DateTimeField('date offer ends')



    
