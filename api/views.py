from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

# Create your views here.
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'All Customers': '/all_customers/',
        'All Subsciptions': '/all_subscriptions',
        'Specific Customer': 'get_customer/<str:id>/',
        'Specific Subscription': 'get_subscription/<str:id>/',
        'Receive Customer': 'receive_customer/',
    }

    return Response(api_urls)

@api_view(['GET'])
def all_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def all_subscriptions(request):
    subscriptions = Subscription.objects.all()
    serializer = SubscriptionSerializer(subscriptions, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def all_gifts(request):
    gifts = Gifts.objects.all()
    serializer = GiftsSerializer(gifts, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_customer(request, id):
    customer = Customer.objects.get(id=id)
    serializer = CustomerSerializer(customer)

    return Response(serializer.data)


@api_view(['GET'])
def get_subscription(request, id):
    subscription = Subscription.objects.get(id=id)
    serializer = SubscriptionSerializer(subscription)

    return Response(serializer.data)


@api_view(['POST'])
def receive_customer(request):
    data = request.data["customer"]
    serializer = CustomerSerializer(data=data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors)
