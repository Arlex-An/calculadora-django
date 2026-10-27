
"""
Django settings for config project.
"""

import os
from pathlib import Path

# Directorio principal del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent


# Seguridad
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-clave-solo-para-desarrollo"
)

# En Render configura DJANGO_DEBUG=False
DEBUG = os.environ.get("DJANGO_DEBUG", "True").lower() == "true"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
]


# Aplicaciones instaladas
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "suma_app",
    "motos",
]


# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# URLs y plantillas
ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Base de datos
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}


# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# Idioma y zona horaria
LANGUAGE_CODE = "es"
TIME_ZONE = "America/Bogota"

USE_I18N = True
USE_TZ = True


# Archivos estáticos: CSS, JavaScript e imágenes del diseño
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"


# Archivos multimedia: sonidos y documentos subidos
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Configuración de almacenamiento
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage.CompressedManifestStaticFilesStorage"
        ),
    },
}


# Tipo de clave primaria predeterminada
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Correo electrónico para desarrollo
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
