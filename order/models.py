from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField


class PIZZA_SIZE(ChoiceEnum):
    SMALL = 30
    BIG = 50


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField(max_length=1000)

    @classmethod
    def create_customer(cls, f_name=None, l_name=None, address=None):
        """
        create new customer and add it to the database
        :param f_name: customer first_name
        :param l_name: customer last_name
        :param address: customer address
        :return: customer object
        """
        if f_name and l_name and address:
            customer = cls(first_name=f_name, last_name=l_name, address=address)
        customer.save()
        return customer

    def __str__(self):
        return '%s %s place:%s' % (self.first_name, self.last_name, self.address)


class PizzaOrder(models.Model):
    size = EnumChoiceField(enum_class=PIZZA_SIZE, default=PIZZA_SIZE.SMALL)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    @classmethod
    def create_order(cls, pizza_size, customer=None):
        """
        create pizza order, first we have to check existing of the customer
        :param pizza_size: SMALL or BIG
        :param customer: coustomer object
        :return: the created order for this customer
        """
        if customer:
            order = cls(size=pizza_size, customer=customer)
        order.save()
        return order

    @classmethod
    def get_orders(cls, customer):
        """
        get all the orders of this specific customer
        :return: list of orders
        """
        try:
            return cls.objects.filter(customer=customer)
        except Exception:
            return None

    def edit_order(self, pizza_size, customer):
        """
        update the info of the order, including the customer info
        """
        try:
            self.size = pizza_size
            self.customer = customer
            self.save()
        except Exception:
            return None

    def delete_order(self):
        self.delete()

    def __str__(self):
        return "%s %s -- %s size" % (self.customer.first_name, self.customer.last_name, self.size)
