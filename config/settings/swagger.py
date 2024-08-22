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

    'TAGS': [  # 定義標籤
        {'name': 'JWT', 'description': '有關JWT相關的操作'},
        {'name': '用戶管理', 'description': '針對系統所註冊用戶的一些操作'},
        {'name': '角色管理', 'description': '針對系統角色進行數據的操作'},
        {'name': '權限管理', 'description': '針對系統限定權限進行數據的操作'},
        {'name': '菜單管理', 'description': '針對菜單進行數據的操作'},
        {'name': '訂單管理', 'description': '針對訂單進行數據的操作'},
        {'name': '產品管理', 'description': '針對產品進行數據的操作'},
        {'name': '產品種類管理', 'description': '針對產品種類進行數據的操作'},
    ],



}