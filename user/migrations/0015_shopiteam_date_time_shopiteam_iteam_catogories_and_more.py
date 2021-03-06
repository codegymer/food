# Generated by Django 4.0.2 on 2022-04-25 09:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_user_udp'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopiteam',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 4, 25, 9, 43, 59, 324971, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopiteam',
            name='iteam_catogories',
            field=models.CharField(default=datetime.datetime(2022, 4, 25, 9, 44, 29, 988594, tzinfo=utc), max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='udp',
            field=models.ImageField(blank=True, default='udp_pics/udpdefault.jpg', null=True, upload_to='udp_pics'),
        ),
    ]
