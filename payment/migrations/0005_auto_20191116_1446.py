# Generated by Django 2.2.7 on 2019-11-16 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20191116_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='charge',
            old_name='address',
            new_name='street_address1',
        ),
    ]