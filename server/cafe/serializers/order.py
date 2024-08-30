from rest_framework import serializers
from ..models import Menu, Order


class OrderListSerializer(serializers.ModelSerializer):
    class MenuSerializer(serializers.ModelSerializer):
        class Meta:
            model = Menu
            fields = "__all__"

    menu = MenuSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class MenuSerializer(serializers.ModelSerializer):
        class Meta:
            model = Menu
            fields = "__all__"

    menu = MenuSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
