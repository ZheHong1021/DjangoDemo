# swagger.py

SPECTACULAR_SETTINGS = {
    "TITLE": "Django Project",

    # 描述
    "DESCRIPTION": "這是一個測試API的平台",

    # 版本
    "VERSION": "1.0.0", 
    
    "SERVE_INCLUDE_SCHEMA": False,

    # 確保可以使用 form/data
    "POST_PROCESSING_HOOKS": [
        "drf_spectacular.hooks.postprocess_schema_enums",
        "drf_spectacular.hooks.postprocess_schema_customization"
    ],
    
    "COMPONENT_SPLIT_REQUEST": True,  
}