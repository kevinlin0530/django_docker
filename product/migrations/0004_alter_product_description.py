# Generated by Django 4.1.7 on 2023-12-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
    ]