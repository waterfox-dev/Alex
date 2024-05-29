from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

from django.http import HttpRequest

class AdminOrReadOnly(BasePermission):
    
    def has_permission(self, request: HttpRequest, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff

class AdminOrOwner(BasePermission):
    
    def has_object_permission(self, request: HttpRequest, view, obj):
        return request.user.is_staff or obj == request.user
    
    def has_permission(self, request: HttpRequest, view):
        return request.user.is_staff
    
    
class AdminToView(BasePermission):
    
    def has_permission(self, request: HttpRequest, view):
        return request.user.is_staff