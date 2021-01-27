from django.db import models


class Customer(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=100)


class Subscription(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='purchasing_customer')
    plan_name = models.CharField(max_length=100)
    price = models.IntegerField()
    recipient_email = models.CharField(max_length=100)


