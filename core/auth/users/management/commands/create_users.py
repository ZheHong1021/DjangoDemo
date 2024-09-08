from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from core.auth.users.models import CustomUser


class Command(BaseCommand):
    help = '建立 menus資料表的資料'

    def handle(self, *args, **options):
        # 定義要建立的資料
        users = [
            {
                "is_superuser": True,
                "email": "admin@gmail.com",
                "username": "admin",
                "password": "admin1234",
                "is_staff": True,
                "is_active": True,
                "firstname": "系統人員",
                "lastname": None,
                "phone_number": None,
                "age": None,
                "gender": "private",
            },
            {
                "is_superuser": False,
                "email": "guest@gmail.com",
                "username": "guest",
                "password": "guest1234",
                "is_staff": False,
                "is_active": True,
                "firstname": "訪客",
                "lastname": None,
                "phone_number": None,
                "age": None,
                "gender": "private",
            },
        ]


        # 建立的數量
        created_count = 0


        # 將數據一一寫入
        for user in users:
            try:
                # get_or_create() 方法會返回一個元組，第一個元素是 group_instance，第二個元素是 created
                instance, created = CustomUser.objects.get_or_create(
                    **user
                )

                # 還要處理 password
                instance.set_password(user["password"])

                # 如果 created 為 True，則 created_count 加 1
                created_count += 1 if created else 0

                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"生成 users 數據時發生錯誤！錯誤訊息：{e}"))
                continue
        

        
        

        self.stdout.write(self.style.SUCCESS(f"成功生成 users 數據！(共 {created_count}筆)"))