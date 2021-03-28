from django.contrib import admin
from django.urls import path, include
from apps.docs import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls')),
    path('', include('rest_framework.urls')),
    path('api/docs', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
