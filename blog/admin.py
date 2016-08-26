from django.contrib import admin
from .models import Post #importamos el metodo Post 

# Register your models here.

admin.site.register(Post)#hacemos visible en la pag. admin y registramos el modelo

