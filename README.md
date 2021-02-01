# PizzeriaDjangoDANG

Proyecto Pizzeria en Django, Daniel Lopez, Adrian Luces, Nestor Angeles y Giovanni Alcala.

Recordar hacer "py manage.py migrate" para evitar errores al iniciar

ENDPOINTS para el frontend

GET:
Lista Ordenes: localhost:8000/orders
Detalle Orden (Pizzas en la orden): localhost:8000/orders/${id}
Ventas por ingrediente:             localhost:8000/ordersbytop/${topping}
Ventas por tamaño de pizza: localhost:8000/ordersbysize/${size}

(En principio solo de prueba):
Lista Toppings: localhost:8000/toppings
Lista Pizzas: localhost:8000/pizzas

POST:
Añadir Orden (+ Pizzas integradas): localhost:8000/orders

(En principio solo de prueba):
Añadir Topping: localhost:8000/toppings
Añadir Pizza: localhost:8000/pizzas
