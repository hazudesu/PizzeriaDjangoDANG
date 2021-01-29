from django.http import response
from pizzastore.serializers import ToppingSerializer, PizzaSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from pizzastore.models import Topping, Pizza, Order

'''API para manejo de requests sobre Ordenes, Toppings y Pizzas'''


class ToppingListView(APIView):
    '''Obtener lista de Toppings disponibles'''
    permission_classes = (AllowAny,)

    def get(self, request):
        toppings = Topping.objects.all()
        toppings_serializer = ToppingSerializer(toppings, many=True)
        return Response(toppings_serializer.data)
    '''Crear Topping (no necesario, implementado por terminos de prueba)'''

    def post(self, request):
        data = request.data
        serializer = ToppingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PizzaListView(APIView):
    '''Obtener lista de Pizzas Vendidas
    '''
    permission_classes = (AllowAny,)

    def get(self, request):
        pizzas = Pizza.objects.all()
        pizzas_serializer = PizzaSerializer(pizzas, many=True)
        return Response(pizzas_serializer.data)

    '''Crear Pizza (Cambiar)
    '''

    def post(self, request):
        '''Probablemente cambiar para que el campo de topping sea un .add()
        '''
        data = request.data
        serializer = PizzaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderListView(APIView):
    '''Obtener lista de Ordenes Realizadas
    '''
    permission_classes = (AllowAny,)

    def get(self, request):
        orders = Order.objects.all()
        orders_serializer = OrderSerializer(orders, many=True)
        return Response(orders_serializer.data)

    '''Crear Orden (Cambiar)
    '''

    def post(self, request):
        data = request.data
        '''Serializo y guardo en la BD la parte de Orden de la data entrante por la request
        '''
        order_serializer = OrderSerializer(data=data)
        if order_serializer.is_valid():
            final_order = order_serializer.save()

            made_order = order_serializer.data
            '''Recorro el array de pizzas de request.data 
            y procedo a crear un nuevo objeto al que le añado el id de la orden recien creada +
            los campos de pizza previamente incluidos en la pizza en cuestion de request.data
            '''
            for pizza in data["pizzas"]:

                temp_pizza = Pizza()
                temp_pizza.in_order = final_order
                temp_pizza.pizza_size = pizza["pizza_size"]
                temp_pizza.price = pizza["price"]
                temp_pizza.save()
                for topping in pizza["toppings"]:
                    temp_pizza.toppings.add(
                        Topping.objects.get(name=topping["name"])
                    )
                # this prob not needed, se puede guardar directamente temp_pizza
                temp_pizza.save()

            return Response(made_order, status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
