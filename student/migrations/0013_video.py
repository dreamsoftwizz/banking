# Generated by Django 2.0 on 2020-05-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_registration_prefferedtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'video',
            },
        ),
    ]
