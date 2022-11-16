# Generated by Django 4.1.3 on 2022-11-16 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_user_cars_user_cars'),
    ]

    operations = [
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