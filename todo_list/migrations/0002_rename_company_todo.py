# Generated by Django 4.1.4 on 2022-12-10 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Company',
            new_name='Todo',
        ),
    ]
