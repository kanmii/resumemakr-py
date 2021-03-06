# -*- coding: utf-8 -*-

"""
Django settings for server project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their config, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from typing import Tuple

from django.utils.translation import ugettext_lazy as ugt

from server.settings.components import BASE_DIR, config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

SECRET_KEY = config("SECRET_KEY")

# Application definition:

INSTALLED_APPS: Tuple[str, ...] = (
    # Your apps go here:
    "server.apps.accounts.apps.AccountsConfig",
    "server.apps.resumes.apps.ResumesConfig",
    # Default django apps:
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # django-admin:
    "django.contrib.admin",
    "django.contrib.admindocs",
    # Health checks:
    # You may want to enable other checks as well,
    # see: https://github.com/KristianOellegaard/django-health-check
    "health_check",
    "health_check.db",
    "health_check.cache",
    "health_check.storage",
    "django.contrib.postgres",
    "corsheaders",
    "graphene_django",
)

MIDDLEWARE: Tuple[str, ...] = (
    # Django:
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "server.middlewares.set_graphql_context_middleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "server.urls"

WSGI_APPLICATION = "server.wsgi.application"


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

USE_I18N = True
USE_L10N = True

LANGUAGES = (("en", ugt("English")),)

LOCALE_PATHS = ("locale/",)

USE_TZ = True
TIME_ZONE = "UTC"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)


# Templates
# https://docs.djangoproject.com/en/2.2/ref/templates/api

TEMPLATES = [
    {
        "APP_DIRS": True,
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # Contains plain text templates, like `robots.txt`:
            BASE_DIR.joinpath("server", "templates")
        ],
        "OPTIONS": {
            "context_processors": [
                # Default template context processors:
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ]
        },
    }
]

# Media files
# Media-root is commonly changed in production
# (see development.py and production.py).

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.joinpath("media")


# Django authentication system
# https://docs.djangoproject.com/en/2.2/topics/auth/

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
]


# Security
# https://docs.djangoproject.com/en/2.2/topics/security/

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True  # <- blocking graphiql must be False in dev
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = "DENY"

# Timeouts
EMAIL_TIMEOUT = 5


GRAPHENE = {"SCHEMA": "logics.graphql_schema.graphql_schema"}
