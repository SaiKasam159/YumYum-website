# Generated by Django 3.0.6 on 2020-06-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddiary', '0019_remove_activity_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='fooddiary/images/'),
        ),
    ]
