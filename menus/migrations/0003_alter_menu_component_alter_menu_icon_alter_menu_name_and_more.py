# Generated by Django 5.0.4 on 2024-06-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_menu_is_menu_menu_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='component',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='菜單路由組件'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='icon',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='菜單圖案'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='菜單路由名稱'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='path',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='菜單路由路徑'),
        ),
    ]
