# Generated by Django 4.1.3 on 2022-12-17 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0018_leaverequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signupform',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='signupform',
            name='last_name',
        ),
    ]