# Generated by Django 2.0 on 2020-05-19 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_auto_20200518_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
