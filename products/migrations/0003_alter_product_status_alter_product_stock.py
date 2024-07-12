# Generated by Django 5.0.4 on 2024-07-12 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productcategory_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('available', '銷售中'), ('out_of_stock', '缺貨中'), ('discontinued', '停售')], default='out_of_stock', max_length=20, verbose_name='訂單狀態'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, default=0, verbose_name='產品庫存'),
        ),
    ]
