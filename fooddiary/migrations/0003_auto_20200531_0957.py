# Generated by Django 3.0.6 on 2020-05-31 09:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fooddiary', '0002_auto_20200523_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 5, 31, 9, 57, 21, 242736, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
