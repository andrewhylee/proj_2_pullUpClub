# Generated by Django 3.0.4 on 2020-03-29 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pullupclub', '0004_auto_20200329_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='arm_length_inches',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='award',
            name='threshold_to_achieve',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
