# Generated by Django 2.1.3 on 2018-12-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20181226_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(choices=[(2, 'High'), (1, 'Moderate'), (0, 'Low')], default=2),
        ),
    ]
