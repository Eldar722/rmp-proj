# Generated by Django 5.1.2 on 2024-10-30 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf_app', '0010_alter_cake_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cake',
            options={'verbose_name': 'Пирог', 'verbose_name_plural': 'Пироги'},
        ),
    ]