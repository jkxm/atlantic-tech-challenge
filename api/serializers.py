from .models import *
from rest_framework import serializers


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer()
    gifts = SubscriptionSerializer(many=True)

    class Meta:
        model = Customer
        fields = [
            'id', 'first_name', 'last_name',
            'address_1', 'address_2', 'city',
            'state', 'postal_code', 'subscription',
            'gifts'
        ]



