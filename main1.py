import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def getallorders():
    try:
        db = firestore.client()
        orders = db.collection("USERS").document("UID1").collection("ORDERS")
        docs = orders.stream()
        list1 = []
        for doc in docs:
            list1.append(doc.to_dict())
        return list1
    except:
        return "Data not returned"


def getallcollections():
    try:
        db = firestore.client()
        orders = db.collection("USERS").document("UID1").collection(
            "ORDERS").where('status', '==', 'Delivered')
        docs = orders.stream()
        list2 = []
        customers = []
        for doc in docs:
            if doc.to_dict()['customerid'] in list2:
                pass
            else:
                list2.append(doc.to_dict()['customerid'])
        for c in list2:
            documents = db.collection("USERS").document("UID1").collection(
                "CUSTOMERS").where('customerid', '==', c).stream()
            for doc in documents:
                # .order_by("name", direction=firestore.Query.DESCENDING)
                customers.append(doc.to_dict())
        return customers
    except:
        return "Data not returned"


def getorder(customerid):
    try:
        db = firestore.client()
        orders1 = db.collection("USERS").document("UID1").collection(
            "ORDERS").where('customerid', '==', customerid).stream()
        list2 = []
        for doc in orders1:
            if doc.to_dict()['status'] == 'Delivered':
                list2.append(doc.to_dict())
        return list2
    except:
        return "Data not returned"


def getpay(customerid):
    try:
        db = firestore.client()
        collections1 = db.collection("USERS").document("UID1").collection(
            "COLLECTIONS").where('customerid', '==', customerid).stream()
        list1 = []
        for doc1 in collections1:
            list1.append(doc1.to_dict())
        return list1
    except:
        return "Data not returned"


def getcustomers():
    try:
        db = firestore.client()
        customers = db.collection("USERS").document("UID1").collection(
            "CUSTOMERS").stream()
        list1 = []
        for doc1 in customers:
            list1.append(doc1.to_dict())
        return list1
    except:
        return "Data not returned"


def getproducts():
    try:
        db = firestore.client()
        products = db.collection("PRODUCTS").stream()
        list1 = []
        for doc1 in products:
            list1.append(doc1.to_dict())
        return list1
    except:
        return "Data not returned"


####################################################
####################################################
        #POST REQUESTS#
####################################################
####################################################


def createorder(data):
    try:
        print(data['customerid'])
        db = firestore.client()
        ord_ref = db.collection("USERS").document("UID1").collection(
            "ORDERS")
        ord_ref.add(data)
        return "Order Data Created"
    except:
        return "Error in creating Data"


def createcollection(data):
    try:
        print(data)
        db = firestore.client()
        # cust_ref = db.collection("USERS").document("UID1").collection(
        #     "CUSTOMERS").where("customerid", '==', data['customerid'])
        # op = cust_ref.stream().to_dict()['openingbalance']
        coll_ref = db.collection("USERS").document("UID1").collection(
            "COLLECTIONS")
        coll_ref.add(data)
        return "Collection Data Created"
    except:
        return "Error in creating Data"


def createcustomer(data):
    try:
        print(data)
        db = firestore.client()
        cust_ref = db.collection("USERS").document("UID1").collection(
            "CUSTOMERS")
        print(cust_ref.add(data))
        return "Customer Data Created"
    except:
        return "Error in creating Data"


####################################################
####################################################
        #ADMIN#
####################################################
####################################################


def agetallorders():
    try:
        db = firestore.client()
        count1 = len(list(db.collection("USERS").get()))
        print("Count ", count1)
        list1 = []
        for i in range(1, count1+1):
            orders = db.collection("USERS").document(
                "UID"+str(i)).collection("ORDERS")
            docs = orders.stream()
            for doc in docs:
                list1.append(doc.to_dict())
        return list1
    except:
        return "Data not returned"
    

def agetallcollections():
    try:
        db = firestore.client()
        count1 = len(list(db.collection("USERS").get()))
        print("Count ", count1)
        list1 = []
        for i in range(1, count1+1):
            collections = db.collection("USERS").document(
                "UID"+str(i)).collection("COLLECTIONS")
            docs = collections.stream()
            for doc in docs:
                list1.append(doc.to_dict())
        return list1
    except:
        return "Data not returned"
