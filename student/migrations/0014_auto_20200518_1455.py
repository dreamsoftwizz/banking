# Generated by Django 2.0 on 2020-05-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
