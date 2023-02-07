from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # pass
    fieldsets=(
        (None, {'fields':('username', 'password')}),
        ('Información Personal', {'fields':('first_name','last_name','email')}),
        ('Permisos', {'fields':('is_superuser','is_staff','is_active','groups','user_permissions')}),
        ('Redes Sociales', {'fields':('web_site','twitter','tag_game_name')}),
    )
#Esta contendra atributos a los cuales podmos acceder desde el inspeccionar del navegador
