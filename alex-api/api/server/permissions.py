from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

from django.http import HttpRequest

class AdminOrReadOnly(BasePermission):
    
    def has_permission(self, request: HttpRequest, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff