# Generated by Django 4.0.2 on 2022-04-25 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_shopiteam_iteam_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopiteam',
            name='iteam_image',
            field=models.ImageField(default='iteam_image.jpg', upload_to='iteam_images/'),
        ),
    ]
