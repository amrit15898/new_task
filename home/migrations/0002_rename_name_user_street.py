# Generated by Django 4.1.3 on 2022-11-16 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='street',
        ),
    ]
