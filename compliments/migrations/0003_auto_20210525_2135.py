# Generated by Django 3.1.2 on 2021-05-26 02:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliments', '0002_auto_20210525_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compliments',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]