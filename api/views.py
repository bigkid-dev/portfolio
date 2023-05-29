from django.shortcuts import render
from rest_framework.views import APIView
from business.models import Customer
from rest_framework.response import Response
from .serializers import CustomerSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 
# Create your views here.
class Api_View(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        customers = Customer.published.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response('bad request', status=status.HTTP_400_BAD_REQUEST)
    

class CustomerDetailedView(APIView):

    def get(self, request, pk, format=None):
        customer = Customer.published.get(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
