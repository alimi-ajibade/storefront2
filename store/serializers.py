from dataclasses import fields
from itertools import product
from logging import error
from rest_framework import serializers
from store.models import Cart, CartItem, Product, Collection, Review
from decimal import Decimal


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

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)


class SimpleProductSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax'
    )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()

    total_price = serializers.SerializerMethodField(
        method_name='get_total_price')

    def get_total_price(self, cartitem: CartItem):
        return cartitem.product.unit_price * cartitem.quantity

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']


class AddCartItemSerializer(serializers.ModelSerializer):
    # Because Product id is dynamically generated we have to explicit create its attribute
    product_id = serializers.IntegerField()

    # To Check if the product passed by the user exist
    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value):
            raise serializers.ValidationError(
                'No product with the given ID')
        return value

    def save(self, **kwargs):
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        cart_id = self.context['cart_id']

        try:
            cart_item = CartItem.objects.get(
                cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(
                cart_id=cart_id, **self.validated_data)

        return self.instance  # This is all done to conform to the structure of the method

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(
        method_name='get_total_price')

    def get_total_price(self, cart: Cart):
        return sum([
            item.quantity*item.product.unit_price for item in cart.items.all()
        ])

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']

    # This is set to read only, so that it won,t become a requirement for create collections
    products_count = serializers.IntegerField(read_only=True)
