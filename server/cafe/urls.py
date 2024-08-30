from django.urls import path
from . import views


urlpatterns = [
    path('menus/', views.menu_list),
    path('menus/<int:menu_pk>', views.menu_detail),
    path('menus/create/image/', views.menu_image),
    path('orders/', views.order_list),
    path('orders/<int:order_pk>', views.order_detail),
]