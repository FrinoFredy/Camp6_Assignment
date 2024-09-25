from django.urls import path
from .views import customer_details_view, customer_list, order_list, order_item_list

urlpatterns = [
    path('customers', customer_list),
    path('customers/<int:pk>', customer_details_view),
    path('orders', order_list),
    path('order-items', order_item_list),
]
