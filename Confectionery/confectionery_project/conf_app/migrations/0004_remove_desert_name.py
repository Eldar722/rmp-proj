# Generated by Django 5.1.2 on 2024-10-29 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf_app', '0003_desert_added_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desert',
            name='name',
        ),
    ]
