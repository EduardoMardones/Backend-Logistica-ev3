# transporte/permissions.py
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado:
    - GET, HEAD, OPTIONS: Permitido para todos
    - POST, PUT, PATCH, DELETE: Solo para administradores (staff)
    """
    def has_permission(self, request, view):
        # Métodos seguros permitidos para todos
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Métodos de escritura solo para staff/admin
        return request.user and request.user.is_staff