# Generated by Django 2.0 on 2020-04-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='companylink',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='postlink',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='companyname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='eligibility',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='noofvacancy',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='post',
            field=models.CharField(max_length=200),
        ),
    ]
