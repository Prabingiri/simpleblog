# Generated by Django 3.2.3 on 2021-06-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above To Read Blog Post..', max_length=255),
        ),
    ]
