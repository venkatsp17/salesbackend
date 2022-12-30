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
