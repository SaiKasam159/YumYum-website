# Generated by Django 3.0.6 on 2020-05-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddiary', '0006_auto_20200531_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
