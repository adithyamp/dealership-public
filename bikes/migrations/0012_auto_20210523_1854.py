# Generated by Django 2.2 on 2021-05-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0011_auto_20210518_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bike',
            name='description',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bike',
            name='phone_number',
            field=models.CharField(default=234, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bike',
            name='year',
            field=models.CharField(choices=[('2021', '2021'), ('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000'), ('1999', '1999'), ('1998', '1998'), ('1997', '1997'), ('1996', '1996'), ('1995', '1995'), ('Before 1995', 'Before 1995')], max_length=30),
        ),
    ]
