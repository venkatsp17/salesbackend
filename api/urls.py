from mobile.views import orders, collections, custorder, custpay, getcust
from django.urls import path

urlpatterns = [
    path('orders/', orders),
    path('collection/', collections),
    path('details/<id>', custorder),
    path('details1/<id1>', custpay),
    path('customers/', getcust)
]
