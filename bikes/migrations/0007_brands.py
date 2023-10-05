# Generated by Django 2.2 on 2021-05-10 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0006_bike_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
                ('image', models.URLField(null=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
    ]