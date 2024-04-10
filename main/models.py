from django.db import models

# Create your models here.

class User(models.Model):
    UserId = models.BigAutoField(primary_key=True, blank=False, null=False)
    UserName = models.CharField(max_length=300, blank=False, null=False)
    Password = models.CharField(max_length=300, blank=False, null=False)
    Name = models.CharField(max_length=500, blank=False, null=False)
    PhoneNumber = models.CharField(max_length=200, blank=False, null=False)
    Level = models.IntegerField(blank=False, null=False)

class Customer(models.Model):
    CustomerId = models.BigAutoField(primary_key=True, blank=False, null=False)
    CustomerName = models.CharField(max_length=500, blank=False, null=False)
    ContactPerson = models.CharField(max_length=500, blank=True, null=False)
    Address =  models.TextField()
    City = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    Email = models.CharField(max_length=300, blank=True, null=False)
    PhoneNumber1 = models.CharField(max_length=200, blank=False, null=False)
    PhoneNumber2 = models.CharField(max_length=200, blank=True, null=False)
    Pincode = models.CharField(max_length=50)
    State = models.CharField(max_length=300)
    UserId = models.CharField(max_length=100, blank=False, null=False)
    TotalPendingAmount = models.DecimalField(decimal_places=2, max_digits=50)


class Products(models.Model):
    ProductId = models.BigAutoField(primary_key=True, blank=False, null=False)
    ProductName = models.CharField(max_length=200)
    KG = models.IntegerField()
    Price = models.DecimalField(decimal_places=2, max_digits=20, default=0)


class PriceList(models.Model):
    ProductId = models.CharField(max_length=200)
    Price1 =  models.DecimalField(decimal_places=2, max_digits=20)
    Price2 =  models.DecimalField(decimal_places=2, max_digits=20)
    Price3 =  models.DecimalField(decimal_places=2, max_digits=20)


class Orders(models.Model):
    OrderId = models.BigAutoField(primary_key=True, blank=False, null=False)
    CustomerId = models.BigIntegerField(blank=False, null=False)
    CGST = models.DecimalField(decimal_places=2, max_digits=50)
    SGST = models.DecimalField(decimal_places=2, max_digits=50)
    SubTotal = models.DecimalField(decimal_places=2, max_digits=50)
    Total = models.DecimalField(decimal_places=2, max_digits=50)
    DiscountAmount = models.DecimalField(decimal_places=2, max_digits=50)
    OrderDate = models.DateField(auto_now_add=True)
    OrderNotes = models.TextField()
    OrderStatus = models.CharField(max_length=100)
    ProductIds = models.CharField(max_length=500)
    Quantities = models.CharField(max_length=500)
    UserId = models.CharField(max_length=100, blank=False, null=False)

class Collections(models.Model):
    CollectionId = models.BigAutoField(primary_key=True, blank=False, null=False)
    UserId = models.CharField(max_length=100, blank=False, null=False)
    CustomerId = models.BigIntegerField(blank=False, null=False)
    CollectionNotes = models.TextField()
    PaymentMode = models.CharField(max_length=200)
    Amount = models.DecimalField(decimal_places=2, max_digits=50)
    ReceivedDate = models.DateField(auto_now_add=True)


