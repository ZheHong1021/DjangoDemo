from .base import *


# 建議放前面，但因為使用package，因此原本的MIDDLEWARE已經存在，要用 insert添加
# MIDDLEWARE = [ 
#     # ...
#     'corsheaders.middleware.CorsMiddleware', # 需注意与其他中间件顺序，这里放在最前面即可
#     # ...
# ]

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

# 【CORS設定】支持跨域配置开始
CORS_ORIGIN_ALLOW_ALL = True # 允許所有跨站請求, 且whitelist不會被使用
# CORS_ORIGIN_WHITELIST = ( # 設定白名單
#     "http://localhost:8000",
#     "http://localhost",
#     'http://103.118.27.148',
#     'https://103.118.27.148',
# )

CORS_ALLOW_CREDENTIALS = True # 設定為 True 時，允許跨來源資源共用時發送 Cookie。默認值為 False