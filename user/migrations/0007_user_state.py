# Generated by Django 4.0.2 on 2022-04-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_order_delivery_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
