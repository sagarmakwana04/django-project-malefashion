# Generated by Django 4.2.3 on 2023-07-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_product_product_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_pic',
            field=models.ImageField(upload_to='profile_pic/'),
        ),
    ]