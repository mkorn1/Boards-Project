# Generated by Django 3.1.7 on 2021-03-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0010_auto_20210323_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='board',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='starter',
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(max_length=255),
        ),
    ]
