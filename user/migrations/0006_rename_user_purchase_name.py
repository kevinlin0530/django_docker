# Generated by Django 4.1.7 on 2023-12-05 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_id_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='user',
            new_name='name',
        ),
    ]
