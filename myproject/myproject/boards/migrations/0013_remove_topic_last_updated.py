# Generated by Django 3.1.7 on 2021-03-24 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0012_auto_20210324_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='last_updated',
        ),
    ]