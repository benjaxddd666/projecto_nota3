from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('productos', views.productos, name='productos'),
    path('carrito', views.carrito, name='carrito'),
    path('signin', views.signin, name='signin'),
    path('login', views.login, name='login'),
    path('crud', views.crud, name='crud'),
    path('formulario', views.formulario, name='formulario'),
    path('producto_del/<str:pk>', views.producto_del, name='producto_del'),
    path('producto_findEdit/<str:pk>', views.producto_findEdit, name='producto_findEdit'),
    path('productoAdd', views.productoAdd, name='productoAdd'),
    path('productoUpdate/<str:pk>', views.productoUpdate, name='productoUpdate')
    ]