# Generated by Django 3.0.6 on 2020-06-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddiary', '0014_meal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='fooddiary/images'),
        ),
    ]