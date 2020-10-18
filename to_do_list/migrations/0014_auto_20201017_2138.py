# Generated by Django 3.1.2 on 2020-10-18 02:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0013_auto_20201014_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_began',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 17, 21, 38, 42, 73372)),
        ),
        migrations.AlterField(
            model_name='taskrelationship',
            name='relationship_status',
            field=models.CharField(choices=[('after_task', 'after_task'), ('before_task', 'before_task')], max_length=50),
        ),
    ]
