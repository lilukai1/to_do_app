# Generated by Django 3.1.2 on 2021-05-24 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0028_auto_20210524_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', related_query_name='parent', to='to_do_list.project'),
        ),
    ]