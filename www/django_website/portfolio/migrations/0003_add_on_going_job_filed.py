# Generated by Django 3.0.8 on 2022-04-04 20:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_added_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='on_going',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]