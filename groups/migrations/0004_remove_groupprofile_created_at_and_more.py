# Generated by Django 5.0.4 on 2024-06-24 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_groupwithprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupprofile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='groupprofile',
            name='updated_at',
        ),
    ]
