# Generated by Django 3.0.6 on 2020-06-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddiary', '0017_auto_20200608_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='fooddiary/images'),
        ),
    ]
