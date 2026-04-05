from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import CoffeeBeans
from .serializers import CoffeeBeansSerializer
from rest_framework.views import APIView
# Create your views here.
class CoffeeBeansList(generics.ListCreateAPIView):
    queryset=CoffeeBeans.objects.all()
    serializer_class=CoffeeBeansSerializer

    def delete(self,request,*args,**kwargs):
        CoffeeBeans.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class CoffeeBeansListDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=CoffeeBeans.objects.all()
    serializer_class=CoffeeBeansSerializer
    lookup_field="pk"

class CustomCoffeeBeansList(APIView):
    def get(self, request, format=None):
        title= request.query_params.get("varietal","")
        if title:
            coffee_varietal=CoffeeBeans.objects.filter(varietal__icontains=title)        
        else:
            coffee_varietal=CoffeeBeans.objects.all()

        serializer=CoffeeBeansSerializer(coffee_varietal, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)