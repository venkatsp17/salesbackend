from rest_framework import serializers
from main.models import Orders, Customer, Collections, Products, User


class Orderserializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ("OrderId", "CustomerId", "CGST","SGST","SubTotal","Total","DiscountAmount","OrderDate","OrderNotes","OrderStatus","ProductIds","Quantities")


class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("CustomerId", "CustomerName", "ContactPerson","Address","City","Country","Email","PhoneNumber1","PhoneNumber2","Pincode","State","TotalPendingAmount")

class Collectionserializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ("CollectionId", "CustomerId", "CollectionNotes","PaymentMode","Amount","ReceivedDate")

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("ProductId", "ProductName", "KG", "Price")

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("UserId", "UserName", "Password", "Name", "PhoneNumber", "Level")
