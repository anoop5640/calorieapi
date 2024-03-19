from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodItem
from .serializers import FoodItemSerializer
from django.http import Http404

class FoodCalorieView(APIView):
    def get(self, request, name, format=None):
        try:
            food_item = FoodItem.objects.get(name__iexact=name)
            serializer = FoodItemSerializer(food_item)
            return Response(serializer.data)
        except FoodItem.DoesNotExist:
            raise Http404
