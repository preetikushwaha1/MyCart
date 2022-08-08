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


class Contact(models.Model):
    contact_id = models.AutoField(primary_key =True)
    con_name = models.CharField(max_length=60,default=" ")
    con_email = models.CharField(max_length=60,default=" ")
    con_phone = models.CharField(max_length=10, default=" ")
    con_desc = models.CharField(max_length=500,default=" ")

    def __str__(self):
        return self.con_name        #



class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json =models.CharField(max_length=1000)       #storing the items directly in the database

    ord_name = models.CharField(max_length=50,default=" ") 
    ord_email = models.CharField(max_length=50,default=" ")
    ord_phone_no = models.CharField(max_length=10,default=" ")
    ord_Address = models.CharField(max_length=150,default=" ")
    ord_city = models.CharField(max_length=50,default=" ")
    ord_state = models.CharField(max_length=50,default=" ")
    ord_zip_code = models.CharField(max_length=50, default=" " )


    def __str__(self):
        return self.ord_name
