from unittest import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

from order.models import PizzaOrder, Customer
from order.serializers import PizzaOrderSerializer


class ViewTestCase(TestCase):
    """
    test pizza order app endpoint functionality
    """
    def setUp(self):
        """
        Define the test client and other test variables.
        """
        self.client = APIClient()
        self.order_data = {
            "customer": {
                "first_name": "Larosh",
                "last_name": "Tanbari",
                "address": "Coppistr"
            },
            "size": "BIG"
        }
        self.response = self.client.post(
            reverse("get_all_or_create"),
            data=self.order_data,
            format="json"
        )

    def test_create_order_list(self):
        """
        test the order create view
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_order_list(self):
        """
        test the customer orders get view
        """
        customer = Customer.objects.get(first_name="Larosh", last_name="Tanbari")
        orders = PizzaOrder.objects.filter(customer=customer)
        response = self.client.get(
            reverse('order_list',
                    kwargs={'customer': orders.custome}),
            format="json"
        )
        serializer = PizzaOrderSerializer(orders, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_order_list(self):
        """
        test orders get all view
        """
        response = self.client.get(reverse('get_all_or_create'))
        orders = PizzaOrder.objects.all()
        serializer = PizzaOrderSerializer(orders, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_an_order(self):
        """
        test unique order get view
        """
        order = PizzaOrder.objects.get(id=self.response.data['id'])
        response = self.client.get(
            reverse('order_details',
                    kwargs={'order_id': order.id}),
            format="json"
        )

        serializer = PizzaOrderSerializer(order)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_an_order(self):
        """
        test order update view
        """
        order = PizzaOrder.objects.get(id=self.response.data['id'])
        updated_order = {"customer": {
            "first_name": "Lara",
            "last_name": "Tanbari",
            "address": "Coppistr22, 10365 Berlin"
        },
            "size": "SMALL"
        }
        res = self.client.put(
            reverse('order_details',
                    kwargs={'order_id': order.id}),
            updated_order,
            format='json'
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_order(self):
        """
        test order delete view
        """
        order = PizzaOrder.objects.get(id=self.response.data['id'])
        response = self.client.delete(
            reverse('order_details',
                    kwargs={'order_id': order.id}),
            format='json',
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
