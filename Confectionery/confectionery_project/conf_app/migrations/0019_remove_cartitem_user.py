# Generated by Django 5.1.2 on 2024-11-03 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf_app', '0018_cartitem_user_alter_delivery_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
    ]
