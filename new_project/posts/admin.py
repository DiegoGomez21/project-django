from django.contrib import admin
from posts.models import Post

@admin.register(Post) #Esta mandando al panel de administrador que registre post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_at'] #Propiedad que muestra ciertos atributos de nuestro modelo
