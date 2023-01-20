from mobile.views import orders, collections, custorder, custpay, getcust, createord, getproduct, createcoll, createcust
from django.urls import path

urlpatterns = [
    path('orders/', orders),
    path('collection/', collections),
    path('details/<id>', custorder),
    path('details1/<id1>', custpay),
    path('customers/', getcust),
    path('products/', getproduct),
    path('createorder/', createord),
    path('createcollection/', createcoll),
    path('createcustomer/', createcust),
]
