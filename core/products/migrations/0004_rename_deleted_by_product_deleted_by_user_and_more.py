# Generated by Django 5.0.4 on 2024-09-10 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_options_alter_productcategory_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='deleted_by',
            new_name='deleted_by_user',
        ),
        migrations.RenameField(
            model_name='productcategory',
            old_name='deleted_by',
            new_name='deleted_by_user',
        ),
    ]
