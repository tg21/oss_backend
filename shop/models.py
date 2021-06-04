from django.db import models

# Create your models here.

class user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=30,default='admin') # can be admin,buyer,seller
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id) + " : " + self.first_name + " " + self.last_name

class item(models.Model):
    item_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    discount = models.DecimalField(max_digits=2,decimal_places=2) # discount percentage
