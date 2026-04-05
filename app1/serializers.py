from rest_framework import serializers
from .models import CoffeeBeans

class CoffeeBeansSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeBeans
        fields = ["id","varietal","elevation","notes","date"]