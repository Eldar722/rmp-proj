# Generated by Django 5.1.2 on 2024-10-30 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf_app', '0007_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', upload_to='categories/images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='products/images/', verbose_name='Изображение'),
        ),
    ]