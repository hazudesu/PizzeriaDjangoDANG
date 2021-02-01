# PizzeriaDjangoDANG

Proyecto Pizzeria en Django, Daniel Lopez, Adrian Luces, Nestor Angeles y Giovanni Alcala.

Para iniciar el servidor local:

1.  Crear Virtual Enviroment (env)
2.  Instalar las dependencias ubicadas en el requirements.txt con pip
3.  Ubicarse en la carpeta dangpizza (La que tiene el manage.py)
4.  Ingresar el comando "py manage.py migrate" para evitar posibles errores
5.  Correr el servidor con "py manage.py runserver"

ENDPOINTS para el frontend

GET:  
Lista Ordenes:                      localhost:8000/orders  
Detalle Orden (Pizzas en la orden): localhost:8000/orders/${id}  
Ventas por ingrediente:             localhost:8000/ordersbytop/${topping}  
Ventas por tamaño de pizza:         localhost:8000/ordersbysize/${size}  
  
(En principio solo de prueba):  
Lista Toppings:                     localhost:8000/toppings  
Lista Pizzas:                       localhost:8000/pizzas  

POST:  
Añadir Orden (+ Pizzas integradas): localhost:8000/orders

(En principio solo de prueba):  
Añadir Topping:                     localhost:8000/toppings  
Añadir Pizza:                       localhost:8000/pizzas
