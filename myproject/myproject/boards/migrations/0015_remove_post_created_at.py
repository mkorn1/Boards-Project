# Generated by Django 3.1.7 on 2021-03-24 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0014_auto_20210324_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
    ]
