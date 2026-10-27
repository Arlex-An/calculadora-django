
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Panel de administración de Django
    path("admin/", admin.site.urls),

    # Rutas principales de la aplicación de motocicletas
    path("", include("motos.urls")),
]

# Servir archivos multimedia durante el desarrollo local
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )