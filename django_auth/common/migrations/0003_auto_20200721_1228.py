# Generated by Django 3.0.8 on 2020-07-21 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_userprofile_extra_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='extra_data',
            field=models.TextField(default=''),
        ),
    ]
