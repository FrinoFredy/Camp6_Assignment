from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from .models import Customer, Order, OrderItem
from .serializers import CustomerSerializer, OrderSerializer, OrderItemSerializer
from django.shortcuts import get_object_or_404


@csrf_exempt
def customer_list(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        customer_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customer_serializer.data, safe=False)

    elif request.method == "POST":
        request_data = JSONParser().parse(request)
        customer_add_serializer = CustomerSerializer(data=request_data)
        if customer_add_serializer.is_valid():
            customer_add_serializer.save()
            return JsonResponse(customer_add_serializer.data, status=201)
        return JsonResponse(customer_add_serializer.errors, status=400)


@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        order_lists = Order.objects.all()
        order_list_serializer = OrderSerializer(order_lists, many=True)
        return JsonResponse(order_list_serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        add_order_serializer = OrderSerializer(data=request_data)
        if add_order_serializer.is_valid():
            add_order_serializer.save()
            return JsonResponse(add_order_serializer.data, status=201)
        return JsonResponse(add_order_serializer.errors, status=400)


@csrf_exempt
def order_item_list(request):
    if request.method == "GET":
        order_items = OrderItem.objects.all()
        order_item_serializer = OrderItemSerializer(order_items, many=True)
        return JsonResponse(order_item_serializer.data, safe=False)

    elif request.method == "POST":
        request_data = JSONParser().parse(request)
        add_order_item_serializer = OrderItemSerializer(data=request_data)
        if add_order_item_serializer.is_valid():
            add_order_item_serializer.save()
            return JsonResponse(add_order_item_serializer.data, status=201)
        return JsonResponse(add_order_item_serializer.errors, status=400)


@csrf_exempt
def customer_details_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "GET":
        customer_serializer = CustomerSerializer(customer)
        return JsonResponse(customer_serializer.data, safe=False)

    elif request.method == "PUT":
        request_data = JSONParser().parse(request)
        customer_update_serializer = CustomerSerializer(customer, data=request_data)
        if customer_update_serializer.is_valid():
            customer_update_serializer.save()
            return JsonResponse(customer_update_serializer.data, status=200)
        return JsonResponse(customer_update_serializer.errors, status=400)

    elif request.method == "DELETE":
        customer.delete()
        return HttpResponse(status=204)
