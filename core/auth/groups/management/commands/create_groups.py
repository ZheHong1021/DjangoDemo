from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from core.auth.groups.models import GroupProfile


class Command(BaseCommand):
    help = '建立 menus資料表的資料'

    def handle(self, *args, **options):
        # 定義要建立的資料
        groups = [
            {
                "name": "admin",
            },
            {
                "name": "guest",
            },
        ]

        group_profiles = [
            {
                "name_zh": "系統管理員",
            },
            {
                "name_zh": "訪客",
            },
        ]

        # 建立的數量
        created_count = 0


        # 將數據一一寫入
        for index, group in enumerate(groups):
            # get_or_create() 方法會返回一個元組，第一個元素是 group_instance，第二個元素是 created
            group_instance, created = Group.objects.get_or_create(**group)
            GroupProfile.objects.get_or_create(
                group=group_instance,
                **group_profiles[index]
            )
        

        # 如果 created 為 True，則 created_count 加 1
        created_count += 1 if created else 0
        

        self.stdout.write(self.style.SUCCESS(f"成功生成 groups 數據！(共 {created_count}筆)"))