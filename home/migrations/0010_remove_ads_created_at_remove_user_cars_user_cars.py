# Generated by Django 4.1.2 on 2022-11-16 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_ads_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cars',
        ),
        migrations.AddField(
            model_name='user',
            name='cars',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='home.car'),
            preserve_default=False,
        ),
    ]
