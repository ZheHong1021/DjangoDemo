# Generated by Django 5.0.4 on 2024-08-15 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_record_date_order_amount_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
