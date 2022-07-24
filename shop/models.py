from email.policy import default
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField("")
    image = models.ImageField(upload_to="shop/images", default="")

    # below line will return product name to the objects
    def __str__(self):
        return self.product_name            #ex: Ghadi , watch 

