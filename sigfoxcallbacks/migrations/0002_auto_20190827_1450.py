# Generated by Django 2.2.3 on 2019-08-27 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sigfoxcallbacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CallbackData',
            new_name='Callback',
        ),
    ]