# Generated by Django 4.1.2 on 2022-11-16 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_user_cars'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
