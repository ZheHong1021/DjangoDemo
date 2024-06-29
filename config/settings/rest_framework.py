# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        
        # SIMPLE-JWT
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ],

    # Custom Exception
    'EXCEPTION_HANDLER': 'common.exceptions.custom_exception_handler',
    # [DRF Default]
    # 'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    
    # Swagger-UI
    'DEFAULT_SCHEMA_CLASS': "drf_spectacular.openapi.AutoSchema",
    

    # Filter Backend
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter'
    ], 

    # 設定 ordering使用時的參數
    'ORDERING_PARAM': 'ordering',  # 排序參數


    # 【換頁限制】
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',

    # 日期時間格式
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
}