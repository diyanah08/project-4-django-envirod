# Generated by Django 2.2.4 on 2019-11-15 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_delete_customisedcartitem'),
        ('shop', '0002_customiseditem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomisedItem',
        ),
    ]