from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from main1 import  createorder, getproducts, createcollection, createcustomer
from main.models import Orders, Customer, Collections, Products, User
from main.serializers import Orderserializer, Customerserializer, Collectionserializer, Productserializer, Userserializer
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.db.models import Subquery, OuterRef
import jwt
from django.core.management import settings

@csrf_exempt
def ordersapi(request,id=0):
    if request.method == "GET":
        orders = Orders.objects.all()
        order_serializer = Orderserializer(orders,many=True)
        return JsonResponse(order_serializer.data, safe=False)
    elif request.method == "POST":
        order_data = JSONParser().parse(request)
        if order_data["OrderId"] == 0:
            print(order_data["OrderId"])
            orders = Orders.objects.filter(OrderStatus=order_data["Status"])
            order_serializer = Orderserializer(orders,many=True)
            return JsonResponse(order_serializer.data, safe=False)
        else:
            order_serializer = Orderserializer(data=order_data)
            if order_serializer.is_valid():
                order_serializer.save()
                return JsonResponse("Added successfully", safe=False)
            else:
                return JsonResponse("Error adding data", safe=False)
    elif request.method == "PUT":
        order_data = JSONParser().parse(request)
        orders = Orders.objects.get(OrderId=order_data["OrderId"])
        order_serializer = Orderserializer(orders, data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Error updating data", safe=False)
    elif request.method == "DELETE":
        orders = Orders.objects.get(OrderId=id)
        orders.delete()
        return JsonResponse("Deleted successfully")


@api_view(['GET'])
def userorders(request,id=0):
    orders_data = Orders.objects.filter(UserId=id)
    order_serializer = Orderserializer(orders_data, many=True)
    return JsonResponse(order_serializer.data, safe=False)

@api_view(['GET'])
def customerorders(request,id=0):
    orders_data = Orders.objects.filter(CustomerId=id)
    order_serializer = Orderserializer(orders_data, many=True)
    return JsonResponse(order_serializer.data, safe=False)

@api_view(['POST'])
def getcustomerNamebyId(request):
    data = JSONParser().parse(request)
    CustomerData = Customer.objects.get(CustomerId=data["CustomerId"])
    customer_serializer = Customerserializer(CustomerData)
    return JsonResponse(customer_serializer.data, safe=False)


@csrf_exempt
def customerapi(request,id=0):
    if request.method == "GET":
        customers = Customer.objects.all()
        customers_serializer = Customerserializer(customers,many=True)
        return JsonResponse(customers_serializer.data, safe=False)
    elif request.method == "POST":
        customers_data = JSONParser().parse(request)
        customers_serializer = Customerserializer(data=customers_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Error adding data", safe=False)
    elif request.method == "PUT":
        customers_data = JSONParser().parse(request)
        customers = Customer.objects.get(CustomerId=customers_data["CustomerId"])
        customers_serializer = Customerserializer(customers, data=customers_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Updated successfully")
        return JsonResponse("Error updating data", safe=False)
    elif request.method == "DELETE":
        customers = Customer.objects.get(CustomerId=id)
        customers.delete()
        return JsonResponse("Deleted successfully")


@api_view(['GET'])
def usercustomers(request,id=0):
    # customer_data = Customer.objects.filter(UserId=id)
    customer_data = Customer.objects.all()
    customer_serializer = Customerserializer(customer_data, many=True)
    return JsonResponse(customer_serializer.data, safe=False)


@csrf_exempt
def collectionapi(request,id=0):
    if request.method == "GET":
        collection = Collections.objects.all()
        collection_serializer = Collectionserializer(collection,many=True)
        return JsonResponse(collection_serializer.data, safe=False)
    elif request.method == "POST":
        collection_data = JSONParser().parse(request)
        collection_serializer = Collectionserializer(data=collection_data)
        if collection_serializer.is_valid():
            collection_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Error adding data", safe=False)
    elif request.method == "PUT":
        collection_data = JSONParser().parse(request)
        collection = Collections.objects.get(CollectionId=collection_data["CollectionId"])
        collection_serializer = Collectionserializer(collection, data=collection_data)
        if collection_serializer.is_valid():
            collection_serializer.save()
            return JsonResponse("Updated successfully")
        return JsonResponse("Error updating data", safe=False)
    elif request.method == "DELETE":
        collection = Collections.objects.get(CollectionId=id)
        collection.delete()
        return JsonResponse("Deleted successfully")


@api_view(['GET'])
def usercollection(request,id=0):
     # Subquery to get the last added collection for each customer
    last_collection_subquery = Collections.objects.filter(
        CustomerId=OuterRef('CustomerId')
        ).order_by('-ReceivedDate').values('ReceivedDate')[:1]

        # Query to get TotalPendingAmount, CustomerName, CustomerId, and last added collection
    customers_data = Customer.objects.annotate(
        last_collection=Subquery(last_collection_subquery)
        ).filter(TotalPendingAmount__gt=0, last_collection__isnull=False).order_by('last_collection').values('CustomerId', 'CustomerName', 'TotalPendingAmount', 'last_collection')
    return Response(customers_data)

@api_view(['GET'])
def customercollection(request,id=0):
    collection_data = Collections.objects.filter(CustomerId=id)
    collection_serializer = Collectionserializer(collection_data, many=True)
    return JsonResponse(collection_serializer.data, safe=False)



@api_view(['GET'])
def userproducts(request):
    products = Products.objects.all()
    product_serializer = Productserializer(products,many=True)
    return JsonResponse(product_serializer.data, safe=False)


# @api_view(['POST'])
# def createord(request):
#     data = json.loads(request.body)
#     res = createorder(data)
#     if (res == "Order Data Created"):
#         return Response(res, status=200)
#     return Response(res)


# @api_view(['POST'])
# def createcoll(request):
#     data = json.loads(request.body)
#     res = createcollection(data)
#     if (res == "Collection Data Created"):
#         return Response(res, status=200)
#     return Response(res)


# @api_view(['POST'])
# def createcust(request):
#     data = json.loads(request.body)
#     res = createcustomer(data)
#     if (res == "Customer Data Created"):
#         return Response(res, status=200)
#     return Response(res)
from datetime import datetime, timedelta


@api_view(['POST'])
def Login(request):
    data = JSONParser().parse(request)
    userdata = User.objects.get(UserName=data["UserName"])
    user_serializer = Userserializer(userdata)
    if data["Password"] == user_serializer.data["Password"]:
        responseData = user_serializer.data
        # print(responseData)
        payload = {
                'user_id': responseData['UserId'],
                'exp': datetime.utcnow() + timedelta(days=365),  # Adjust expiration as needed
            }
        access_token = jwt.encode(payload=payload,key=settings.SECRET_KEY, algorithm='HS256')
        responseData["access_token"] = access_token
        return JsonResponse(responseData, safe=False)
    else:
        return JsonResponse({"Error":"Username or Password Incorrect"}, safe=False)







