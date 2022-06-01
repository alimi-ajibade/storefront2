from itertools import product
from rest_framework import serializers
from store.models import Product, Collection, Review
from decimal import Decimal


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description', 'product']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    # This is set to read only, so that it won,t become a requirement for create collections
    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'slug',
            'inventory',
            'unit_price',
            'price_with_tax',
            'collection'
        ]

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax'
    )

    # Replaced by Model Serializer
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(
    #     max_digits=6,
    #     decimal_places=2,
    #     source='unit_price'
    # )
    # collection = serializers.PrimaryKeyRelatedField(queryset = Collection.objects.all())
    # collection = serializers.StringRelatedField()
    # collection = CollectionSerializer()
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail',
    # )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # For overwriting the inbuilt validation method in other to parform custom data validations
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('Passowrds do not match')
    #     return 'OK'
