from django.db import models

# Create your models here.

class Producto(models.Model):
	IDProducto      	= models.IntegerField(primary_key=True, unique=True)
	NombreProducto  	= models.CharField(max_length=30, null=False)
	Precio         	 	= models.IntegerField()
	Stock         		= models.IntegerField()
	Categoria       	= models.CharField(max_length=20)
	Imagen         		= models.ImageField(upload_to="imagenes", null=True)
	
	def __str__(self):
		return "Nombre Producto: " + str(self.NombreProducto)
	

class Carrito(models.Model):
	IDCarrito       		= models.IntegerField()
	IDProducto      		= models.ForeignKey('Producto', on_delete=models.CASCADE)
	Cantidad        		= models.IntegerField()
	
	def __str__(self):
		return "ID Producto: " + str(self.IDCarrito)