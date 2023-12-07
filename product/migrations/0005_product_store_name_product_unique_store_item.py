# Generated by Django 4.1.7 on 2023-12-07 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_store_unique_store_name'),
        ('product', '0004_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='store_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='store.store', to_field='name'),
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.UniqueConstraint(fields=('store_name', 'item'), name='unique_store_item'),
        ),
    ]
