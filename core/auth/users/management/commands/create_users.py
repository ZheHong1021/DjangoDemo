from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from core.auth.users.models import CustomUser
from django.contrib.auth.models import Group

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
                "group_name": "admin",
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
                "group_name": "guest",
            },
        ]


        # 建立的數量
        created_count = 0


        # 將數據一一寫入
        for user in users:

            try:
                # 取出 group_name
                group_name = user.pop("group_name", None)

                email = user.get("email")
                instance = CustomUser.objects.filter(email=email).first()


                # 已經存在!
                if instance:
                    self.stdout.write(self.style.WARNING(f"使用者 {email} 已經存在！"))
                    created = False
                else:
                    instance = CustomUser(**user)
                    created = True
                
                    # 還要處理 password
                    instance.set_password(user["password"])
                    instance.save()

                    # 如果 created 為 True，則 created_count 加 1
                    created_count += 1 if created else 0


            except Exception as e:
                self.stdout.write(self.style.ERROR(f"生成 users 數據時發生錯誤！錯誤訊息：{e}"))
        
            

            try:
                # 引用 group
                group_instance = Group.objects.get(
                    name=group_name
                )
                # 將 user 加入 group
                instance.groups.add(group_instance)

                self.stdout.write(self.style.SUCCESS(f"成功綁定 (user={instance.username}, group={group_instance.name})！"))
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"綁定 users與 groups 數據時發生錯誤！錯誤訊息：{e}"))        

        
        

        self.stdout.write(self.style.SUCCESS(f"成功生成 users 數據！(共 {created_count}筆)"))