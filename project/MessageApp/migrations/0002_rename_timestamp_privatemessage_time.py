# Generated by Django 4.2.1 on 2023-05-17 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MessageApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='privatemessage',
            old_name='timestamp',
            new_name='time',
        ),
    ]