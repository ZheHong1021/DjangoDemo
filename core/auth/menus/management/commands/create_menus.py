from django.core.management.base import BaseCommand
from core.auth.menus.models import Menu


class Command(BaseCommand):
    help = '建立 menus資料表的資料'

    def handle(self, *args, **options):
        # 定義要建立的資料
        menus = [
            {
                "priority": 1,
                "title": "儀錶板",
                "name": "Dashboard",
                "path": "/dashboard",
                "component": "Dashboard",
                "redirect": None,
                "icon": "mdi-monitor-dashboard",
                "is_menu": True,
                "is_disabled": False,
                "parent": None
            },
                {
                "priority": 2,
                "title": "WebSocket",
                "name": "WebSocket",
                "path": "/web-socket",
                "component": "WebSocket",
                "redirect": None,
                "icon": "mdi-web-box",
                "is_menu": True,
                "is_disabled": False,
                "parent": None
            },
                {
                "priority": 3,
                "title": "系統管理",
                "name": "Admin",
                "path": "/admin",
                "component": "Admin/Admin",
                "redirect": "/admin/user",
                "icon": "mdi-cog",
                "is_menu": True,
                "is_disabled": False,
                "parent": None
            },
                {
                "priority": 1,
                "title": "用戶管理",
                "name": "UserList",
                "path": "/admin/user",
                "component": "Admin/User/UserList",
                "redirect": "",
                "icon": "mdi-account-box",
                "is_menu": True,
                "is_disabled": False,
                "parent_name": "Admin",
            },
                {
                "priority": 2,
                "title": "角色管理",
                "name": "GroupList",
                "path": "/admin/group",
                "component": "Admin/Group/GroupList",
                "redirect": None,
                "icon": "mdi-account-group",
                "is_menu": True,
                "is_disabled": False,
                "parent_name": "Admin",
            },
            {
                "priority": 3,
                "title": "菜單管理",
                "name": "MenuList",
                "path": "/admin/menu",
                "component": "Admin/Menu/MenuList",
                "redirect": None,
                "icon": "mdi-view-gallery",
                "is_menu": True,
                "is_disabled": False,
                "parent_name": "Admin",
            },
            {
                "priority": 4,
                "title": "權限管理",
                "name": "PermissionList",
                "path": "/permission",
                "component": "Admin/Permission/PermissionList",
                "redirect": None,
                "icon": "mdi-lock",
                "is_menu": True,
                "is_disabled": False,
                "parent_name": "Admin",
            },
                {
                "priority": 6,
                "title": "菜單測試",
                "name": "PathName",
                "path": "/path",
                "component": "Path/PathName",
                "redirect": "",
                "icon": "mdi-menu",
                "is_menu": True,
                "is_disabled": False,
                "parent": None
            },
                {
                "priority": 1,
                "title": "詳細菜單",
                "name": "PathDetail",
                "path": "/path/detail",
                "component": "Path/PathDetail/PathDetail",
                "redirect": "/path/detail/children",
                "icon": "mdi-menu",
                "is_menu": True,
                "is_disabled": False,
                "parent_name": "PathName",
            },
                {
                "priority": 1,
                "title": "詳細子菜單123",
                "name": "PathDetailChildren",
                "path": "/path/detail/children",
                "component": "Path/PathDetail/PathDetailChildren",
                "redirect": None,
                "icon": "mdi-information",
                "is_menu": True,
                "is_disabled": False,
                "parent_name": "PathName",
            },
                {
                "priority": 5,
                "title": "營運管理",
                "name": "Operation",
                "path": "/operation",
                "component": "Operation/Operation",
                "redirect": "/operation/order",
                "icon": "mdi-purse",
                "is_menu": True,
                "is_disabled": False,
                "parent": None
            },
                {
                "priority": 2,
                "title": "訂單管理",
                "name": "OrderList",
                "path": "/operation/order",
                "component": "Operation/Order/OrderList",
                "redirect": None,
                "icon": "mdi-cart-variant",
                "is_menu": True,
                "is_disabled": False,
                "parent_name": "Operation",
            },
                {
                "priority": 1,
                "title": "產品管理",
                "name": "ProductList",
                "path": "/operation/products",
                "component": "Operation/Product/ProductList",
                "redirect": None,
                "icon": "mdi-cart",
                "is_menu": True,
                "is_disabled": False,
                "parent_name": "Operation",
            },
                {
                "priority": 2,
                "title": "產品種類管理",
                "name": "ProductCategoryList",
                "path": "/operation/product-category",
                "component": "Operation/Product/ProductCategoryList",
                "redirect": None,
                "icon": "mdi-invoice-list",
                "is_menu": True,
                "is_disabled": False,
                "parent_name": "Operation",
            },
                {
                "priority": 3,
                "title": "客戶瀏覽",
                "name": "Client",
                "path": "/client",
                "component": "Client/Client",
                "redirect": "/client/product",
                "icon": "mdi-account-multiple",
                "is_menu": True,
                "is_disabled": False,
                "parent": None
            },
                {
                "priority": 1,
                "title": "產品清單",
                "name": "ClientProductList",
                "path": "/client/product",
                "component": "Client/Product/ClientProductList",
                "redirect": "",
                "icon": "mdi-cart",
                "is_menu": True,
                "is_disabled": False,
                "parent_name": "Client",
            },
                {
                "priority": 4,
                "title": "錯誤管理",
                "name": "ErrorView",
                "path": "/error",
                "component": "Errors/ErrorView",
                "redirect": None,
                "icon": "mdi-alert-circle",
                "is_menu": True,
                "is_disabled": False,
                "parent": None
            },
                {
                "priority": 1,
                "title": "401",
                "name": "401_Unauthorized",
                "path": "/error/401",
                "component": "Errors/ErrorView/401_Unauthorized",
                "redirect": None,
                "icon": "",
                "is_menu": True,
                "is_disabled": False,
                "parent_name": "ErrorView"
            },
                {
                "priority": 2,
                "title": "403",
                "name": "403_Forbidden",
                "path": "/error/403",
                "component": "Errors/ErrorView/403_Forbidden",
                "redirect": None,
                "icon": None,
                "is_menu": True,
                "is_disabled": False,
                "parent_name": "ErrorView"
            },
                {
                "priority": 4,
                "title": "500",
                "name": "500_InternalServerError",
                "path": "/error/500",
                "component": "Errors/ErrorView/500_InternalServerError",
                "redirect": None,
                "icon": None,
                "is_menu": True,
                "is_disabled": False,
                "parent_name": "ErrorView"
            },
                    {
                    "priority": 3,
                    "title": "404",
                    "name": "404_NotFound",
                    "path": "/error/404",
                    "component": "Errors/ErrorView/404_NotFound",
                    "redirect": None,
                    "icon": None,
                    "is_menu": True,
                    "is_disabled": False,
                    "parent_name": "ErrorView"
                    }
        ]

        # 建立的數量
        created_count = 0


        # 將數據一一寫入
        for menu in menus:
            # 如果有 parent_name，則先取得 parent 的 instance，再將 parent_name 刪除
            if menu.get("parent_name", None):
                try:
                    # 取得 parent 的 instance
                    menu["parent"] = Menu.objects.get(
                        name=menu["parent_name"]
                    )
                except Menu.DoesNotExist as e:
                    self.stdout.write(self.style.ERROR(f'找不到 parent_name 為 {menu["parent_name"]} 的 menu！'))
                    continue

                # 刪除 parent_name
                del menu["parent_name"]

            # 會回傳一個元組，第一個元素是 menu_instance，第二個元素是 created
            instance, created = Menu.objects.get_or_create(**menu)

            # 如果 created 為 True，則 created_count 加 1
            created_count += 1 if created else 0
        

        self.stdout.write(self.style.SUCCESS(f"成功生成 menus 數據！(共 {created_count}筆)"))