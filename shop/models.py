from django.db import models
from django.contrib.postgres.fields.array import ArrayField
from django.utils import timezone

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=12,)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    emailId = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    isBlocked = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=4,decimal_places=2,default=00.00)
    role = models.CharField(max_length=30,default='admin') # can be admin,buyer,seller
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)


    def _getLoginView(self,auth='authorized'):
        return {
                    'auth' : auth,
                    'username' : self.username,
                    'role' : self.role,
                    'first_name' : self.first_name,
                    'last_name' : self.last_name,
                }

    def __str__(self):
        return str(self.id) + " :-> " + self.first_name + " (" +  self.username + ") " + self.last_name

class item(models.Model):
    item_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    discount = models.DecimalField(max_digits=4,decimal_places=2,default=00.00) # discount percentage
    added_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('category',on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=4,decimal_places=2,default=00.00)
    img_url = models.CharField(max_length=100,null=True)
    tags = ArrayField(models.CharField(max_length=25))
    def __str__(self):
        return str(self.id) + " :-> " + self.item_name

class inventory(models.Model):
    user_id = models.ForeignKey('user',on_delete=models.CASCADE)
    item_id = models.ForeignKey('item',on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id) + " :-> " + self.user_id + " " + self.item_id

class cart(models.Model):
    user_id = models.ForeignKey('user',on_delete=models.CASCADE)
    item_id = models.ForeignKey('item',on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id) + " :-> " + self.user_id + " " + self.item_id

class category(models.Model):
    category = models.CharField(max_length=20)
    def __str__(self):
        return str(self.id) + " :-> " + self.category

class order(models.Model):
    user_id = models.ForeignKey('user',on_delete=models.CASCADE)
    item_id = models.ForeignKey('item',on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=timezone.now)
    payment_mode = models.CharField(max_length=20,default="cash")
    status = models.CharField(max_length=20,default="pending")

    def __str__(self):
        return str(self.id) + " :-> " + self.user_id + " " + self.item_id + " " + self.status

