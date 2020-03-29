# Generated by Django 3.0.4 on 2020-03-28 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pullupclub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='pullUpCount',
        ),
        migrations.RemoveField(
            model_name='student',
            name='record_date',
        ),
        migrations.AddField(
            model_name='student',
            name='nickname',
            field=models.CharField(default='Anonymous', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='Sam Doe', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.CreateModel(
            name='PullUpSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_of_pullups', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pullupclub.Student')),
            ],
        ),
    ]