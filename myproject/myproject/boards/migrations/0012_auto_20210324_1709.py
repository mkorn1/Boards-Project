# Generated by Django 3.1.7 on 2021-03-24 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0011_auto_20210323_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.CharField(max_length=4000),
        ),
    ]
