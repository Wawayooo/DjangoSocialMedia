# Generated by Django 5.0.6 on 2024-12-25 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebBuilder', '0006_rename_content_comment_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
    ]
