from django.contrib import admin
from django.urls import path, re_path, include
from config.django.base import DEBUG # 用於判斷目前開發模式

# 全域URL (不管 DEBUG)
urlpatterns = [
    path("api/", include('orders.urls')),
    path("api/", include('users.urls')),
    path("api/", include('groups.urls')),
    path("api/", include('menus.urls')),
    path("api/token/", include('jwt_auth_token.urls')),
]



# DEBUG = True(Deployment)
if( DEBUG ):
    # 【Debug_Toolbar】
    import debug_toolbar
    # 【Swagger UI】
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

    urlpatterns += [
        path('admin/', admin.site.urls),
        # Debug_Toolbar
        path('__debug__/', include(debug_toolbar.urls)),

        # Swagger-UI
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    ]

    
# DEBUG = False(Production)
else:
    urlpatterns += [
    ]
    pass