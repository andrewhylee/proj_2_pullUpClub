# Generated by Django 3.0.4 on 2020-03-28 19:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pullupclub', '0002_auto_20200328_0455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pullupsession',
            name='amount_of_pullups',
        ),
        migrations.AddField(
            model_name='pullupsession',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pullupsession',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 19, 25, 0, 625650, tzinfo=utc)),
        ),
    ]
