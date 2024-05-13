# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        
        # SIMPLE-JWT
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ],
    
    # Swagger-UI
    'DEFAULT_SCHEMA_CLASS': "drf_spectacular.openapi.AutoSchema",
}