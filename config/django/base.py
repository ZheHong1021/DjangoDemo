"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""



import environ
import os


from config.env import BASE_DIR, env

# Take environment variables from .env file
env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env.bool('DJANGO_DEBUG', default=True)

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': { # MySQL(預設)
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': env('MYSQL_DATABASE'), # MySQL 資料庫的名稱
        'USER': env('MYSQL_USER'), # 使用者名稱
        'PASSWORD': env('MYSQL_PASSWORD'), # 密碼
        'HOST': env('DB_HOST', default='db'), # IP 地址
        'PORT': env('DB_PORT', default='3306'), # 埠號(mysql為 3306)
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    },
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[])

#region (Application definition)
# Local apps
LOCAL_APPS = [
    'users',
    'orders',
]

# Thired party apps
THIRD_PARTY_APPS  = [
    'corsheaders', # corsheaders
    'rest_framework', # rest_framework
    'rest_framework_simplejwt', # simple_jwt
    'django_filters', # filters(排序、搜尋)
    'django_extensions', # 全局自定義管理擴展的存儲庫
    'drf_spectacular', # Swagger UI
    'channels', # websocket
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]


#endregion

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#region (Custom User)
AUTH_USER_MODEL = "users.CustomUser"
#endregion

# Third APP Configuration
from config.settings.cors_header import *
from config.settings.rest_framework import *
from config.settings.simple_jwt import *
from config.settings.swagger import *
from config.settings.debug_toolbar import *
from config.settings.channels import *