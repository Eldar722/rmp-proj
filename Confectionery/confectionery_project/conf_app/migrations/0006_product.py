# Generated by Django 5.1.2 on 2024-10-30 09:37

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf_app', '0005_buns_cakes_cookies_cupcakes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.CharField(max_length=80, verbose_name='Цена')),
                ('added_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время поступления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conf_app.category', verbose_name='Выберите категорию')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
