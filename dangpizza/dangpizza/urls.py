"""dangpizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from pizzastore.api import ToppingListView, PizzaListView, OrderListView, OrderDetailView, SalesbyToppingsView, SalesbySizeView

router = routers.DefaultRouter()


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('pizzastore/', include('pizzastore.urls')),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^toppings/$', ToppingListView.as_view()),
    url(r'^pizzas/$', PizzaListView.as_view()),
    url(r'^orders/$', OrderListView.as_view()),
    url(r'^orders/(?P<id>\d+)/$', OrderDetailView.as_view()),
    url(r'^ordersbytop/(?P<topping>\w{1,50})/$',
        SalesbyToppingsView.as_view()),
    url(r'^ordersbysize/(?P<pizza_size>\w{1,50})/$',
        SalesbySizeView.as_view()),
]
