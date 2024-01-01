import stripe

from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Order
from .utils import get_good_by_type


stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeIntentView(APIView):
    def post(self, request, *args, **kwargs):
        customer = stripe.Customer.create(email=request.data.get('email'))

        good = get_good_by_type(kwargs)
        try:
            intent = stripe.PaymentIntent.create(
                amount=int(good.price * 100),
                currency=good.currency,
                customer=customer['id'],
                metadata={'payment_id': good.id},
                payment_method_types=["card"],
            )
            if isinstance(good, Order):
                good.products.clear()
            return Response({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return Response({'error': str(e)})


class AddToOrderView(APIView):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('id'))
        order = Order.objects.filter(owner_id=request.user.id).first()
        if not order:
            order = Order.objects.create(owner_id=request.user.id)
        order.products.add(product)
        return Response("Product successfully added to an order", status=200)
