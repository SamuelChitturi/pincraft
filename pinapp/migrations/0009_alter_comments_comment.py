# Generated by Django 4.2.7 on 2023-12-11 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinapp', '0008_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(max_length=100),
        ),
    ]
