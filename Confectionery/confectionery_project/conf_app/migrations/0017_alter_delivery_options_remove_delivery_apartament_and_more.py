# Generated by Django 5.1.2 on 2024-11-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf_app', '0016_alter_delivery_address_alter_delivery_apartament_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name': 'Доставка', 'verbose_name_plural': 'Доставки'},
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='apartament',
        ),
        migrations.AddField(
            model_name='delivery',
            name='apartment',
            field=models.CharField(default='', max_length=20, verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='address',
            field=models.CharField(default='', max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='comm_for_order',
            field=models.CharField(default='', max_length=255, verbose_name='Комментарий к заказу'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='entrance',
            field=models.CharField(default='', max_length=20, verbose_name='Подъезд'),
        ),
    ]
