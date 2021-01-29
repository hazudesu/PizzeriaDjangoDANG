from django.db.models import fields
from rest_framework import serializers
from pizzastore.models import Order, Pizza, Topping

'''Serializadores para el procesamiento de data proveniente de los requests del frontend
'''


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'client_id', 'order_date', 'order_price')


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('__all__')


class PizzaSerializer(serializers.ModelSerializer):
    #toppings = ToppingSerializer(read_only=True, many=True)

    class Meta:
        model = Pizza
        fields = ('id', 'in_order', 'pizza_size', 'toppings', 'price')

        # Prob override create method añadiendo un pizza.toppings.add(toppings.objects.get(name='toppings'))
