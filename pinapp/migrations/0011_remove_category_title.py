# Generated by Django 4.2.7 on 2023-12-11 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinapp', '0010_board_pin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
    ]
