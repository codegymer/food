# Generated by Django 4.0.2 on 2022-04-25 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_user_udp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='udp',
            field=models.ImageField(default='udpdefault.jpg', upload_to='udp_pics'),
        ),
    ]
