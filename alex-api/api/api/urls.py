"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from rest_framework import routers

from server.viewset import AuthorViewSet
from server.viewset import ShelfViewSet
from server.viewset import PublisherViewSet
from server.viewset import BookStateViewSet
from server.viewset import BookAvailabilityViewSet
from server.viewset import BookViewSet
from server.viewset import BookViewSet

router = routers.DefaultRouter()

router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'shelves', ShelfViewSet, basename='shelf')
router.register(r'editions', PublisherViewSet, basename='edition')
router.register(r'bookstates', BookStateViewSet, basename='bookstate')
router.register(r'bookavailabilities', BookAvailabilityViewSet, basename='bookavailability')
router.register(r'books', BookViewSet, basename='book')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
