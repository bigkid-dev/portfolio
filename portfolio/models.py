from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

Gender_Choice = (
        ('M', 'male'),
        ('F', 'female'),
    )

Status = (
    ('draft', 'Draft'),
    ('published', 'Published')
)

class PublishedManager(models.Manager):

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


# Create your models here.
class Customer(models.Model):
   
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50, choices=Gender_Choice, default='Male')
    date = models.DateTimeField(default=datetime.now())
    stack = models.CharField(max_length=50, default='Flutter')
    programing = models.TextField()
    status= models.CharField(max_length=50, default='published')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "Portfolio",
        verbose_name_plural = "Portfolios"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)