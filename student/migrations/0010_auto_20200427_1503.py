# Generated by Django 2.0 on 2020-04-27 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20200419_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.CharField(default='', max_length=900),
        ),
    ]
