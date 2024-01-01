from django.urls import path

from .api import StripeIntentView, AddToOrderView
from .views import LandingPageView, ProductListView, OrderListView

urlpatterns = [
    path('stripe_payment_intent/<int:id>/<str:type>/', StripeIntentView.as_view(), name='stripe_payment_intent'),
    path('landing/<int:id>/<str:type>/', LandingPageView.as_view(), name='landing'),
    path('products/', ProductListView.as_view(), name='products'),
    path('add_to_order/<int:id>/', AddToOrderView.as_view(), name='add_to_order'),
    path('see_order/<int:id>/', OrderListView.as_view(), name='see_order'),
]

