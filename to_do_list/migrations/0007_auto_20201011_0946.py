# Generated by Django 3.1.2 on 2020-10-11 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0006_auto_20201011_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_began',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 11, 9, 46, 0, 406725)),
        ),
    ]
