# Generated by Django 3.0.6 on 2020-06-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddiary', '0015_auto_20200607_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='fooddiary/images'),
        ),
    ]