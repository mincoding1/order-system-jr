from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image_src = models.TextField()


class Order(models.Model):
    quantity = models.IntegerField()
    request_detail = models.TextField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="orders")
