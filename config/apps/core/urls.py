from django.urls import path, include

urlpatterns = [
    path('shop/', include('apps.shop.urls'))
]
