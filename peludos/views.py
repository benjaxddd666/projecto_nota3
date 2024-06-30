from django.shortcuts import render, redirect
from .models import Producto,Carrito
from django.urls import reverse
# Create your views here.

def index(request):
    productos= Producto.objects.all()
    context={"productos":productos}
    return render(request, 'peludos/index.html', context)

def login(request):
        productos=Producto.objects.all()
        carrito=Carrito.objects.all()
        context={"login":login}

        return render(request, 'peludos/login.html',context)

def signin(request):
        productos=Producto.objects.all()
        carrito=Carrito.objects.all()
        context={"productos":productos}

        return render(request, 'peludos/signin.html',context)

def carrito(request):
        productos=Producto.objects.all()
        carrito=Carrito.objects.all()
        context={"productos":productos}

        return render(request, 'peludos/carrito.html',context)

def formulario(request):
    productos= Producto.objects.all()
    context={"productos":productos}
    return render(request, 'peludos/formulario.html', context)

def productos(request):
    productos= Producto.objects.all()
    print(productos)
    context={"productos":productos}
    return render(request, 'peludos/productos.html', context)

def crud(request):
  
    productos= Producto.objects.all()
    
    context={"productos":productos}
    return render(request, 'peludos/crud.html', context)
    
def productos(request):
    productoscomidaseca= Producto.objects.raw('SELECT * FROM peludos_producto WHERE Categoria = "Comida Seca"')
    productosjuguetes= Producto.objects.raw('SELECT * FROM peludos_producto WHERE Categoria = "Juguetes"')
    productosaccesorio= Producto.objects.raw('SELECT * FROM peludos_producto WHERE Categoria = "Accesorio"')
    print(productosjuguetes)
    print(productoscomidaseca)
    print(productosaccesorio)
    context={"productoscomidaseca":productoscomidaseca,"productosjuguetes":productosjuguetes,"productosaccesorio":productosaccesorio}
    return render(request, 'peludos/productos.html', context)

def producto_del(request, pk):
      context={}
      try:
            producto=Producto.objects.get(IDProducto=pk)

            producto.delete()
            mensaje ="bien,datos eliminados"
            context = {'mensaje' : mensaje}
            return redirect(reverse('crud'))
      except:
            mensaje = "Error, id de producto no existe"
            context = {'mensaje' : mensaje}
            return redirect(reverse('crud'))
      
def producto_findEdit(request,pk):
      if pk != "":
            producto=Producto.objects.get(IDProducto = pk)
            context = {'producto':producto}
            if producto:
                return render(request,'peludos/formulario_editar.html', context)
            else:
                context={'mensaje':"error"}
                return render(request,'peludos/crud.html', context)

def productoAdd(request):
      if request.method != "POST":
            productos=Producto.objects.all()
            context={'productos':productos}
            return render(request, 'peludos/formulario_agregar.html', context)
      else:
            nombreProducto=request.POST["NombreProducto"]
            precio=request.POST["Precio"]
            stock=request.POST["Stock"]
            categoria=request.POST["Categoria"]
            imagen=request.FILES["Imagen"]
            obj=Producto(NombreProducto=nombreProducto,
                                        Precio=precio,
                                        Stock=stock,
                                        Categoria=categoria,   
                                        Imagen=imagen
            )
            obj.save() 
            return redirect(reverse('crud'))
        
def productoUpdate(request,pk):
      if request.method == "POST":
            producto = Producto.objects.get(IDProducto = pk)
            nombreProducto=request.POST["NombreProducto"]
            precio=request.POST["Precio"]
            stock=request.POST["Stock"]
            categoria=request.POST["Categoria"]

            producto.NombreProducto = nombreProducto
            producto.Precio = precio
            producto.Stock = stock
            producto.Categoria = categoria
            producto.save()
            return redirect(reverse('crud'))
        
