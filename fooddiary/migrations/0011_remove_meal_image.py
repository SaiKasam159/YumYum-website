# Generated by Django 3.0.6 on 2020-06-07 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fooddiary', '0010_meal_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='image',
        ),
    ]
