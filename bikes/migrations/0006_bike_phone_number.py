# Generated by Django 2.2 on 2021-05-08 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0005_bike_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
