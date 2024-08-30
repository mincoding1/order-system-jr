from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .serializers.menu import MenuListSerializer, MenuSerializer
from .serializers.order import OrderListSerializer, OrderSerializer
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from .models import Menu, Order


@api_view(["GET", "POST"])
def menu_list(request):
    if request.method == "GET":
        menus = get_list_or_404(Menu)
        serializer = MenuListSerializer(menus, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PATCH", "DELETE"])
def menu_detail(request, menu_pk):
    menu = get_object_or_404(Menu, pk=menu_pk)
    if request.method == "GET":
        serializer = MenuSerializer(menu)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        menu.delete()
        data = {"delete": f"menu {menu_pk} is deleted"}
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def menu_image(request):
    file = request.FILES["file"]
    fs = FileSystemStorage()
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_file_name = f"{now}{file.name}"
    filename = fs.save(new_file_name, file)
    return Response({"filename": filename}, status=status.HTTP_201_CREATED)


@api_view(["GET", "POST"])
def order_list(request):
    if request.method == "GET":
        orders = get_list_or_404(Order)
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        menu = get_object_or_404(Menu, pk=request.data["menu_id"])
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(menu=menu)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PATCH", "DELETE"])
def order_detail(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    if request.method == "GET":
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == "PATCH":
        menu = get_object_or_404(Menu, pk=request.data["menu_id"])
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(menu=menu)
            return Response(serializer.data)
    elif request.method == "DELETE":
        order.delete()
        data = {"delete": f"order {order_pk} is deleted"}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
