# Generated by Django 2.2 on 2021-05-17 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0009_auto_20210512_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownership', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='bike',
            name='ownership',
            field=models.ForeignKey(default=1234, on_delete=django.db.models.deletion.CASCADE, to='bikes.Ownership'),
            preserve_default=False,
        ),
    ]
