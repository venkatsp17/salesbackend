from main import views
from django.urls import path, re_path

urlpatterns = [
    path('login/', views.Login),
    path('orders/', views.ordersapi),
    re_path(r'^orders/([0-9]+)$', views.ordersapi),
    re_path(r'^uorders/([0-9]+)$', views.userorders),
    re_path(r'^corders/([0-9]+)$', views.customerorders),
    re_path(r'^getcustdata/',views.getcustomerNamebyId),
    path('customers/', views.customerapi),
    re_path(r'^customers/([0-9]+)$', views.customerapi),
    re_path(r'^ucustomers/([0-9]+)$', views.usercustomers),
    path('collections/', views.collectionapi),
    re_path(r'^collections/([0-9]+)$', views.collectionapi),
    re_path(r'^ucollections/([0-9]+)$', views.usercollection),
    re_path(r'^ccollections/([0-9]+)$', views.customercollection),
    path('products/', views.userproducts),
    # path('products/', getproduct),
    # path('createorder/', createord),
    # path('createcollection/', createcoll),
    # path('createcustomer/', createcust),

]
