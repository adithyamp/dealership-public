# Generated by Django 2.2 on 2021-04-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0002_bike_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='price',
            field=models.IntegerField(default=2020),
            preserve_default=False,
        ),
    ]
