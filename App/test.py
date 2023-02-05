from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

@api_view(['GET'])
def getData(request):
  
  #if not firebase_admin._apps:
  cred = credentials.Certificate("./ServiceAccount.json")
  app = firebase_admin.initialize_app(cred)

  db = firestore.client()
  ref = db.collection(u'users')
  docs = ref.stream()

  for doc in docs:
    if doc.get('id') == "1":
      res = u'{} => {}'.format(doc.id, doc.to_dict())
      
    """
    print(
        f"doc:{doc.id} "
        f"id:{doc.get('id')} "
        f"name:{doc.get('name')} "
        )
    """
  
  return Response(res)