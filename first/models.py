from django.db import models

class user(models.Model):
    user_id=models.IntegerField(max_length=10)
    user_name=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    price=models.FloatField(max_length=10)
    cuisine=models.IntegerField(max_length=1)
    taste=models.IntegerField(max_length=1)
    healthy=models.IntegerField(max_length=10)
    orders=models.IntegerField(max_length=10)
    menu=models.CharField(max_length=100)

class dishes(models.Model):
    dishes_number=models.IntegerField(max_length=10)
    dishes_name=models.CharField(max_length=50)
    dishes_img=models.ImageField()
    dishes_price=models.FloatField(max_length=10)
    dishes_cursine=models.IntegerField(max_length=1)
    dishes_taste=models.IntegerField(max_length=1)
    dishes_healthy=models.IntegerField(max_length=10)
    dishes_hot=models.IntegerField(max_length=10)

class evaluation(models.Model):
    user_id = models.IntegerField(max_length=10)
    user_name = models.CharField(max_length=50)
    comment=models.CharField(max_length=128)

class dishing(models.Model):
    order_number=models.IntegerField(max_length=5)
    user_id=models.IntegerField(max_length=10)
    order=models.CharField(max_length=128)

class UserToken(models.Model):
    user=models.OneToOneField(to='user',on_delete=models.CASCADE)
    token=models.CharField(max_length=64)


# Create your models here.
