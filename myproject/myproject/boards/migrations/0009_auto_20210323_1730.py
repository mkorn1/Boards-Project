# Generated by Django 3.1.7 on 2021-03-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0008_auto_20210323_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
