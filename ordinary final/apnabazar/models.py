from django.db import models

# Create your models here.


class Product(models.Model):
    p_id = models.IntegerField()
    p_name=  models.CharField(max_length=50)
    p_description = models.CharField(max_length=50)
    p_price = models.IntegerField()
    p_discount = models.IntegerField(default=0)


