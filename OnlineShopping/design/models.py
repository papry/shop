from django.db import models

from django.db import models

class category(models.Model):
    Category_name=models.CharField(max_length=250,default="")

class Supplier(models.Model):
    Supplier_name = models.CharField(max_length=250, default="")
    Address = models.CharField(max_length=250, default="")
    Phone_no = models.IntegerField( default=2000)
class Product(models.Model):
    Category = models.ForeignKey(category,on_delete='CASCADE')
    Supplier = models.ForeignKey(Supplier, on_delete='CASCADE')
    Product_name = models.CharField(max_length=250, default="")
    description = models.CharField(max_length=250, default="")
    Stock = models.IntegerField(default=20000)
    Price = models.IntegerField( default="")
class Admin(models.Model):
    Product = models.ForeignKey(Product,on_delete='CASCADE')
    Admin_name = models.CharField(max_length=250, default="")
    Password = models.CharField(max_length=250, default="")
class Customer(models.Model):
    Product = models.ForeignKey(Product, on_delete='CASCADE')
    Customer_name = models.CharField(max_length=250, default="")
    Email= models.CharField(max_length=250, default="")
    Password = models.CharField(max_length=250, default="")
    Phone_no= models.CharField(max_length=250, default="")
class Payment(models.Model):
    Customer = models.ForeignKey(Customer, on_delete='CASCADE')
    Payment_type = models.CharField(max_length=250, default="")
    Payment_date = models.CharField(max_length=250, default="")
    Quantity = models.IntegerField(default="")
    Amount = models.IntegerField(default="")






