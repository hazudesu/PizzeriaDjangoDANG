from django.db import models

# Create your models here.

'''Modelo de Orden'''


class Order(models.Model):
    client_id = models.CharField(max_length=10)
    order_date = models.DateTimeField(auto_now_add=True)
    order_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)


'''Modelo de Topping(Ingresados manualmente de manera previa)'''


class Topping(models.Model):
    name = models.CharField(max_length=60, unique=True)
    topping_price = models.DecimalField(
        max_digits=4, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


'''Modelo de Pizzas'''


class Pizza(models.Model):
    in_order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, blank=True, related_name="pizzas")
    pizza_size = models.CharField(
        max_length=3,
        choices=(
            ("sm", "small"),
            ("m", "medium"),
            ("lg", "large")
        ),
    )
    toppings = models.ManyToManyField(
        Topping, blank=True, related_name="pizzast")
    price = models.DecimalField(
        max_digits=4, decimal_places=2, default=0.00)
