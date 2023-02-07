from django.db import models
from django.db import models
#Vamos a crear nuestro modelo de usuarios
from django.contrib.auth.models import AbstractUser


#No le añadiremos ninguna propiedad

class User(AbstractUser):
    email = models.EmailField(unique=True) #Necesita ser unica
    web_site = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    tag_game_name = models.CharField(max_length=20, blank=True)
    USERNAME_FIELD = 'email' #Son los campos necesarios
    REQUIRED_FIELDS = []
