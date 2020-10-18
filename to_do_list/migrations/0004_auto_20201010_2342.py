# Generated by Django 3.1.2 on 2020-10-11 04:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('to_do_list', '0003_auto_20201010_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_began',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 10, 23, 42, 3, 793043)),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
