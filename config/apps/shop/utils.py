from django.shortcuts import get_object_or_404

from rest_framework.response import Response

from .models import Product, Order


def get_good_by_type(kwargs: dict):
    type_ = kwargs.get('type')
    if type_ not in ['order', 'product']:
        return Response('No such type of payment', status=404)
    if type_ == 'product':
        good = get_object_or_404(Product, id=kwargs.get("id"))
    else:
        good = get_object_or_404(Order, id=kwargs.get('id'))
    return good
