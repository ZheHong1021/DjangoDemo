# Generated by Django 5.0.4 on 2024-09-10 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_delete_groupwithprofile_groupprofile_deleted_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupprofile',
            old_name='deleted_by',
            new_name='deleted_by_user',
        ),
    ]
