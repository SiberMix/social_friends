from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Friend Service API",
        default_version='v1',
        description="API для управления друзьями в социальной сети",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('friends.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
