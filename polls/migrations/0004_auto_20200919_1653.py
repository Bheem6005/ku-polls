# Generated by Django 3.1.1 on 2020-09-19 09:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200919_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 19, 9, 53, 41, 286110, tzinfo=utc)),
        ),
    ]
