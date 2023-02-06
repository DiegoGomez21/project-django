from rest_framework.permissions import BasePermission

class IdAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        
        elif request.method == "POST":
            return True
        
        else:    
            return request.user.is_staff #Aqui retornamos false si el usuario no es adimnistrador