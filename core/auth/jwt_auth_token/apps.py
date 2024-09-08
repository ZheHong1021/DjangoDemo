from django.apps import AppConfig


class JwtAuthTokenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.auth.jwt_auth_token'
