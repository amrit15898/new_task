# Generated by Django 4.1.3 on 2022-11-16 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_user_cars_user_cars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cars',
        ),
    ]
