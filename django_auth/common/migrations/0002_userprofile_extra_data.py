# Generated by Django 3.0.8 on 2020-07-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='extra_data',
            field=models.CharField(default='', max_length=255),
        ),
    ]