from rest_framework import generics,mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.mixins import StaffEditorPermissionMixin,UserQuerySetMixin
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.ListCreateAPIView,
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    def perform_create(self , serializer_class):
        title = serializer_class.validated_data.get('title')
        content = serializer_class.validated_data.get('content') or None
        if content is None:
            content = title
        serializer_class.save(user=self.request.user,content=content)

    # def get_queryset(self ,*args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     # print(request.user)
    #     return qs.filter(user = request.user)

class ProductDetailAPIView(StaffEditorPermissionMixin,UserQuerySetMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(StaffEditorPermissionMixin,UserQuerySetMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content :
            instance.content = instance.title

class ProductDestroyAPIView(StaffEditorPermissionMixin,UserQuerySetMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_destroy(self,instance):
        super().perform_destroy(instance)

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    UserQuerySetMixin,
    generics.GenericAPIView,
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get(self , req, *args , **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(req,*args , **kwargs)
        return self.list(req,*args , **kwargs)

    def post(self,req,*args , **kwargs):
        return self.create(req,*args , **kwargs)

    def delete(self,req,*args , **kwargs):
        return self.destroy(req,*args , **kwargs)
    
    def put(self , req , *args , **kwargs):
        return self.update(req,*args , **kwargs)

@api_view(['GET','POST'])
def product_alt_view(req,pk = None):
    if req.method == "GET" :
        if pk is not None :
            queryset = Product.objects.filter(pk=pk)
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset , many = True).data
        return Response(data)
    if req.method == "POST":
        serializer = ProductSerializer(data = req.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid_data":"Not good data"},status=400)