from forex_python.converter import CurrencyRates

from django.db import models

from django.contrib.auth.models import User


class Product(models.Model):
    CURRENCY_CHOICES = (
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
    )

    name = models.CharField(default='', max_length=255, verbose_name='Item name')
    description = models.TextField(default='', verbose_name='Item description')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0, verbose_name='Item price')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD', verbose_name='Item currency')

    def __str__(self):
        return self.name


class Discount(models.Model):
    code = models.CharField(max_length=20, default='Default', verbose_name='Discount code')
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Discount percent')

    def __str__(self):
        return self.code


class Tax(models.Model):
    code = models.CharField(max_length=20, default='Default', verbose_name='Tax code')
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Tax percent')

    def __str__(self):
        return self.code


class Order(models.Model):
    products = models.ManyToManyField(Product, verbose_name='Ordered products')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name="Order\'s owner")
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def price(self):
        return self.get_total()

    @property
    def currency(self):
        return 'USD'

    def get_subtotal(self):
        usd_subtotal = 0
        c = CurrencyRates()
        for product in self.products.all():
            if product.currency == 'USD':
                usd_subtotal += product.price
            else:
                usd_subtotal += c.convert('EUR', 'USD', product.price)
        return usd_subtotal

    def get_discount_amount(self):
        if self.discount:
            return self.get_subtotal() * self.discount.amount / 100
        return 0

    def get_tax_amount(self):
        if self.tax:
            return (self.get_subtotal() - self.get_discount_amount()) * self.tax.amount / 100
        return 0

    def get_total(self):
        return self.get_subtotal() - self.get_discount_amount() + self.get_tax_amount()

    def __str__(self):
        return f'Order #{self.pk}'
