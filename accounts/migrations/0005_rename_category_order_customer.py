# Generated by Django 4.0.5 on 2022-07-11 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_order_category_alter_order_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='category',
            new_name='customer',
        ),
    ]
