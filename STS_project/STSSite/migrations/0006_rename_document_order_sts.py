# Generated by Django 4.1.6 on 2023-02-19 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('STSSite', '0005_rename_user_order_person_alter_order_date_to_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='document',
            new_name='sts',
        ),
    ]
