# Generated by Django 3.2.3 on 2021-06-03 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_auto_20210603_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='pinintrest_url',
            new_name='pinterest_url',
        ),
    ]
