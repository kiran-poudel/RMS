from django.db import models
from django.contrib.auth.models import AbstractUser,Group

# Create your models here.

class User(AbstractUser):
    email = models.EmailField()
    groups = models.ForeignKey(Group,on_delete=models.SET_NULL,null=True,blank=True)
    username = models.CharField(max_length=300,unique=True)
    password = models.CharField(max_length=300)
    image = models.FileField()
    address = models.CharField(max_length=300)
    contact = models.CharField(max_length=300)


class MenuCategory(models.Model):
    name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(MenuCategory, on_delete=models.SET_NULL,null=True)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Order(models.Model):
    waiter = models.ForeignKey('Waiter',on_delete=models.SET_NULL,null=True,blank=True)
    category = models.ForeignKey(MenuCategory,on_delete=models.SET_NULL,null=True)
    name = models.ForeignKey(MenuItem,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.category.name}"



class Waiter(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    contact = models.CharField(max_length=300)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Reception(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=300)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
class Bill(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    price =models.ForeignKey(MenuItem,on_delete=models.SET_NULL,null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.id}"
