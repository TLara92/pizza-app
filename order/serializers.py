from rest_framework import serializers
from enumchoicefield import EnumChoiceField

from .models import PizzaOrder, Customer, PIZZA_SIZE


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'address')


class PizzaOrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer() # nested serializer - one to many relationship

    class Meta:
        model = PizzaOrder
        fields = '__all__'

    size = EnumChoiceField(enum_class=PIZZA_SIZE)

    """
    create/ update functions are used to return complete object instances 
    based on the validated data to create or update the complete object
    """
    def create(self, validated_data):
        customer_data = validated_data.pop('customer', None)
        customer_model = Customer.objects.create(**customer_data)
        order = PizzaOrder.objects.create(customer=customer_model, **validated_data)
        return order

    def update(self, instance, validated_data):
        customer_data = validated_data.pop('customer', None)
        customer = instance.customer  # the old customer data
        instance.customer.first_name = customer_data.get('first_name', customer.first_name)
        instance.customer.last_name = customer_data.get('last_name', customer.last_name)
        instance.customer.address = customer_data.get('address', customer.address)
        instance.size = validated_data.get('size', instance.size)

        if customer_data is not None:
            instance.edit_order(pizza_size=instance.size, customer=instance.customer)

        instance.save()
        return instance