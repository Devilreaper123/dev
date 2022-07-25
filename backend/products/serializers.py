from rest_framework import serializers
from .models import Product
from .validators import validate_title,validate_title_no_hello,unique_product_title
from api.serializers import UserPublicSerializer

class ProductInLineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name= 'product-detail',
        lookup_field = 'pk',
        read_only = True,
        # request = 
    )
    title = serializers.CharField(read_only = True)

class ProductSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source ='title' , read_only = True)
    # email = serializers.EmailField(source = 'user.email' , read_only= True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    # related_products = ProductInLineSerializer(source = 'user.product_set.all',read_only = True, many=True)
    # my_discount = serializers.SerializerMethodField(read_only = True)
    owner = UserPublicSerializer(source = 'user',read_only = True)
    title = serializers.CharField(validators =[unique_product_title,validate_title_no_hello])
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='product-edit',
        lookup_field = 'pk'
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field = 'pk'
        )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='product-delete',
        lookup_field = 'pk'
    )
    class Meta:
        model = Product
        fields = [
            #'my_user_data',
            #'email',
            #'my_discount',
            #'related_products',
            'id',
            'owner',
            'delete_url',
            'edit_url',
            'url',
            'title',
            'price',
            'content',
            'sale_price',
            
        ]

    def get_my_user_data(self,obj):
        return {
            "username":obj.user.username,
            "ID":obj.user.id
        }

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"'{value}' is already a product name")
    #     return value

    # def create(self,validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(obj,email)
    #     return obj

    # def update(self,instance,validated_data):
    #     email = validated_data.pop('email')
    #     instance.title = validated_data.get('title')
    #     return super().update(instance , validated_data)

    # def get_edit_url(self,obj):
    #     # return f"http://localhost:4000/api/products/{obj.id}"
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("product-edit",kwargs = {"pk":obj.pk} , request = request)

    # def get_my_discount(self,obj):
    #     if not hasattr(obj , 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.get_discount()