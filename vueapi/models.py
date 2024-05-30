from django.db import models


# Create your models here.

class Character(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    color = models.CharField(max_length=10, help_text='应援色',default='')

    def __str__(self):
        return self.name


class GoodsIP(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    goodsIp = models.ForeignKey('GoodsIP', on_delete=models.CASCADE,default='')
    producer = models.CharField(max_length=30, help_text='生产商')
    type = models.CharField(max_length=20, help_text='谷子类型')
    productDate = models.TextField()
    series = models.CharField(max_length=50, help_text='来自系列')
    size = models.CharField(max_length=50, help_text='谷子尺寸')
    character = models.ForeignKey('Character',on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.name
