from products.serializers import ProductSerializer
from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(["POST"])
def api_home(request):
    data = request.data
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid_data":"Not good data"},status=400)

