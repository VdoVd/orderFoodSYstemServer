from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    account_id=models.IntegerField(primary_key=True)

class customer(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    account_id=models.IntegerField(primary_key=True)

class User_Profile(models.Model):
    avatar = models.CharField(max_length=200)
    nickName = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    monitor=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    profile_id = models.IntegerField(primary_key=True)
    account_id = models.IntegerField()