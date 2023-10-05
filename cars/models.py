from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


years_list = (
    ('2022',"2022"),
    ('2021',"2021"),
    ('2020',"2020"),
    ('2019',"2019"),
    ('2018',"2018"),
    ('2017','2017'),
    ('2016',"2016"),
    ('2015',"2015"),
    ('2014',"2014"),
    ('2013',"2013"),
    ('2012',"2012"),
    ('2011',"2011"),
    ('2010',"2010"),
    ('2009',"2009"),
    ('2008',"2008"),
    ('2007',"2007"),
    ('2006',"2006"),
    ('2005',"2005"),
    ('2004',"2004"),
    ('2003',"2003"),
    ('2002',"2002"),
    ('2001',"2001"),
    ('2000',"2000"),
    ('1999',"1999"),
    ('1998',"1998"),
    ('1997',"1997"),
    ('1996',"1996"),
    ('1995',"1995"),
    ('Before 1995',"Before 1995"),
)


class Car(models.Model):
    brand = models.ForeignKey('CarBrand', on_delete=models.CASCADE)
    model_name = models.CharField(max_length=300)
    kms_driven = models.PositiveIntegerField()
    year = models.CharField(choices=years_list, max_length=30)
    fuel_type = models.ForeignKey('CarFuel', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    transmission = models.ForeignKey('CarTransmission', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ownership = models.ForeignKey('CarOwnership', on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.model_name


class CarBrand(models.Model):
    brand_name = models.CharField(max_length=200)
    image = models.URLField()

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Car brand'
        verbose_name_plural = 'Car brands'


class CarFuel(models.Model):
    fuel_name = models.CharField(max_length=200)

    def __str__(self):
        return self.fuel_name

    class Meta:
        verbose_name = 'Car fuel'
        verbose_name_plural = 'Car fuels'


class CarTransmission(models.Model):
    transmission_name = models.CharField(max_length=200)

    def __str__(self):
        return self.transmission_name

    class Meta:
        verbose_name = 'Car transmission'
        verbose_name_plural = 'Car transmissions'


class CarOwnership(models.Model):
    ownership_name = models.CharField(max_length=200)

    def __str__(self):
        return self.ownership_name

    class Meta:
        verbose_name = 'Car Ownership'
        verbose_name_plural = 'Car Ownerships'
