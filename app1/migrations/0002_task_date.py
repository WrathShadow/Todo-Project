# Generated by Django 3.2 on 2021-05-12 02:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.date(2021, 5, 12)),
        ),
    ]