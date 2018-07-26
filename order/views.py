from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import PizzaOrder
from .serializers import PizzaOrderSerializer


@api_view(['GET', 'POST'])
def get_all_or_create(request):
    """
    :return: List of all orders or create new order
    """
    if request.method == 'GET':
        try:
            orders = PizzaOrder.objects.all()
        except PizzaOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PizzaOrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PizzaOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def order_list(request, customer_id):
    """
    :return: List of customer orders
    """
    if request.method == 'GET':
        try:
            orders = PizzaOrder.objects.filter(customer=customer_id)
        except PizzaOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PizzaOrderSerializer(orders, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def order_details(request, order_id):
    """
    :return: specific order, update or delete order
    """
    try:
        order = PizzaOrder.objects.get(id=order_id)
    except PizzaOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PizzaOrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PizzaOrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)