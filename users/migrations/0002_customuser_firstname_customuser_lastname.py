# Generated by Django 5.0.4 on 2024-05-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='firstname',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='名字'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='lastname',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='姓氏'),
        ),
    ]
