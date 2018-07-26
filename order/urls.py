from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from order.views import order_list, order_details, get_all_or_create

urlpatterns = [
    # Get_All orders or create new one
    url(r'^orders/$', get_all_or_create , name='get_all_or_create'),
    # Get_All_Customer_Orders
    url(r'^orders/(?P<customer_id>[0-9]+)$', order_list, name='order_list'),
    # Get/Update/Delete specific order
    url(r'^order/(?P<order_id>[0-9]+)$', order_details, name='order_details'),
]