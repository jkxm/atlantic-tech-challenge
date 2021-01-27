from .models import *
from rest_framework import serializers


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'plan_name', 'price']


class GiftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gifts
        fields = ['id', 'plan_name', 'price', 'recipient_email']


class CustomerSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer()
    gifts = GiftsSerializer(many=True)

    class Meta:
        model = Customer
        fields = [
            'id', 'first_name', 'last_name',
            'address_1', 'address_2', 'city',
            'state', 'postal_code',
            'subscription', 'gifts'
        ]

    def create(self, validated_data):
        subscription = validated_data.pop('subscription')
        gifts = validated_data.pop('gifts')

        customer, created = Customer.objects.update_or_create(**validated_data)

        Subscription.objects.update_or_create(customer=customer, id=subscription['id'], defaults=subscription)

        for gift in gifts:
            Gifts.objects.update_or_create(customer=customer, id=gift['id'], defaults=gift)

        return customer
