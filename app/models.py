from django.db import models

# Create your models here.
class lsurls(models.Model):
    long =models.CharField(max_length=400)
    short = models.CharField(max_length=40)
    nick = models.CharField(max_length=60,null=True)
    created = models.DateTimeField(auto_now_add=True)
