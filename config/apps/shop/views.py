from django.conf import settings
from django.views.generic import TemplateView

from .models import Product, Order
from .utils import get_good_by_type


class OrderListView(TemplateView):
    template_name = 'shop/order.html'

    def get_context_data(self, *args, **kwargs):
        order = Order.objects.prefetch_related('products').filter(owner_id=kwargs.get('id')).first()
        context = super(OrderListView, self).get_context_data(**kwargs)
        context.update(
            {
                'order': order
            }
        )
        return context


class LandingPageView(TemplateView):
    template_name = 'shop/landing.html'

    def get_context_data(self, *args, **kwargs):
        good = get_good_by_type(kwargs)
        context = super(LandingPageView, self).get_context_data(**kwargs)
        context.update(
            {
                'type': kwargs.get('type'),
                'good': good,
                'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
            }
        )
        return context


class ProductListView(TemplateView):
    template_name = 'shop/products.html'

    def get_context_data(self, *args, **kwargs):
        products = Product.objects.all()
        context = super(ProductListView, self).get_context_data(**kwargs)
        context.update(
            {
                'products': products
            }
        )
        return context


