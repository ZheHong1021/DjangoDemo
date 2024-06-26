# Generated by Django 5.0.4 on 2024-06-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_remove_groupprofile_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupprofile',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='name_zh',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
