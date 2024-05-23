from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from server.viewset import AuthorViewSet
from server.viewset import ShelfViewSet
from server.viewset import PublisherViewSet
from server.viewset import BookStateViewSet
from server.viewset import BookViewSet
from server.viewset import UserViewSet

from server.views import ApiView

SchemaView = get_schema_view(
    openapi.Info(
        title="Alex API", default_version="v1", 
        description="Alex API is the main interface to interact with Alex database.",  
        license=openapi.License(name = "CC BY-NC-SA 4.0")
    )
)

router = routers.DefaultRouter()

router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'shelves', ShelfViewSet, basename='shelf')
router.register(r'editions', PublisherViewSet, basename='edition')
router.register(r'bookstates', BookStateViewSet, basename='bookstate')
router.register(r'books', BookViewSet, basename='book')
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),   
    path('swagger/', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', SchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/token',TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh',TokenObtainPairView.as_view(), name='token_refresh_pair'),
    path('api/appqr', ApiView.get_app_qr, name='app_qr')
]
