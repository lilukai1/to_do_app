# Generated by Django 3.1.2 on 2020-10-21 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0019_auto_20201021_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskrelationship',
            name='target_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_task', to='to_do_list.task'),
        ),
    ]