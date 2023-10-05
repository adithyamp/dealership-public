from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


bike_brands = (
    ('Royal Enfield',"Royal Enfield"),
    ('Yamaha',"Yamaha"),
    ('Bajaj',"Bajaj"),
    ('Hero',"Hero"),
    ('Honda',"Honda"),
    ('TVS',"TVS"),
    ('Suzuki',"Suzuki"),
    ('Java',"Java"),
    ('KTM',"KTM"),
    ('Hero Electric',"Hero Electric"),
    ('Ampere',"Ampere"),
    ('Aprilla',"Aprilla"),
    ('Ather',"Ather"),
    ('Avanturaa Choppers',"Avanturaa Choppers"),
    ('Benling',"Benling"),
    ('Benelli',"Benelli"),
    ('BGauss',"BGauss"),
    ('BMW',"BMW"),
    ('CFMoto',"CFMoto"),
    ('Ducati',"Ducati"),
    ('Eeve',"Eeve"),
    ('Evolet',"Evolet"),
    ('F.B Mondial',"F.B Mondial"),
    ('Gemopai',"Gemopai"),
    ('Harley-Davidson',"Harley-Davidson"),
    ('Husqvarna',"Husqvarna"),
    ('Hyosung',"Hyosung"),
    ('Indian',"Indian"),
    ('Joy-e-bike',"Joy-e-bike"),
    ('Kawasaki',"Kawasaki"),
    ('Lectro',"Lectro"),
    ('Mahindra',"Mahindra"),
    ('Moto Guzzi',"Moto Guzzi"),
    ('MV Augusta',"MV Augusta"),
    ('Norton',"Norton"),
    ('Odysse',"Odysse"),
    ('Okinawa',"Okinawa"),
    ('PURE EV',"PURE EV"),
    ('Revolt',"Revolt"),
    ('SWM',"SWM"),
    ('Techo Electra',"Techo Electra"),
    ('Triumph',"Triumph"),
    ('Vespa',"Vespa"),
    ('Yo',"Yo"),
    ('Other Brands',"Other Brands"),
)

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

class Bike(models.Model):
    brand = models.ForeignKey('Brands', on_delete=models.CASCADE)
    model_name = models.CharField(max_length=400)
    kms_driven = models.PositiveIntegerField()
    year = models.CharField(choices=years_list, max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bikes/')
    price = models.PositiveIntegerField()
    ownership = models.ForeignKey('Ownership', on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    posted = models.DateTimeField(default=timezone.now)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.model_name

    def get_absolute_url(self):
        return reverse('bike_list')


class Brands(models.Model):
    brand_name = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Ownership(models.Model):
    ownership = models.CharField(max_length=200)

    def __str__(self):
        return self.ownership

    class Meta:
        verbose_name = 'Ownership'
        verbose_name_plural = 'Ownership'
