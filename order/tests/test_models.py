from django.test import TestCase
from order.models import PizzaOrder, Customer, PIZZA_SIZE


class OrderTestCase(TestCase):
    """
    test pizza order app database models functionality
    """
    def setUp(self):
        """
        create new customer and order
        """
        new_customer = Customer.create_customer("Lara", "Tanbari", "Coppistr22, 10365 Berlin-Germany")
        PizzaOrder.create_order(PIZZA_SIZE.SMALL, customer=new_customer)

    def test_get_orders(self):
        """
        test customer's orders get model function
        """
        customer = Customer.objects.get(first_name="Lara", last_name="Tanbari")
        order = PizzaOrder.get_orders(customer).count()
        self.assertGreater(order, 0, "There should be one or more orders")

    def test_edit_order(self):
        """
        test order update model function
        """
        customer = Customer.objects.get(first_name="Lara", last_name="Tanbari")
        order = PizzaOrder.objects.get(customer=customer)
        new_size = PIZZA_SIZE.BIG
        order.edit_order(new_size, customer)
        self.assertEqual(order.size, new_size, "The order is modified")

    def test_delete_order(self):
        """
        test delete order model function
        """
        customer = Customer.objects.get(first_name="Lara", last_name="Tanbari")
        order = PizzaOrder.objects.get(customer=customer, size=PIZZA_SIZE.SMALL)
        order.delete_order()
        customer = Customer.objects.get(first_name="Lara", last_name="Tanbari")
        d_order = PizzaOrder.objects.filter(size=PIZZA_SIZE.SMALL, customer=customer).count()
        self.assertTrue(d_order == 0, "There should be no order with this specifications")
