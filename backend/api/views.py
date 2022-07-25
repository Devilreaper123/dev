from email import header
from products.serializers import ProductSerializer
from django.shortcuts import render
# from django.http import JsonResponse,HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(["GET","POST"])
def api_home(request):
    # if request.method != 'POST':
    #     return Response({"details":"GET Not allowed"}, status=405)
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(model_data, fields=['id','title','price','sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)
    #     json_data = json.dumps(data)
    # return HttpResponse(json_data , headers = {"content-type":"application/json"}) 