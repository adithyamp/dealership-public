from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import CarBrand, CarFuel, CarOwnership, CarTransmission, Car
from django.core.paginator import Paginator
from .forms import CarForm
from django.contrib.auth.models import User
from django.db.models import Q
from .filters import CarFilter
from django.contrib import messages


def car_list(request):
    car_list = Car.objects.all().order_by('-posted')
    
    # search
    search_query = request.GET.get('c')
    if search_query:
        car_list = car_list.filter(
            Q(model_name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    myfilter = CarFilter(request.GET, queryset=car_list)
    car_list = myfilter.qs

    paginator = Paginator(car_list, 8)   
    page_number = request.GET.get('page')
    car_list = paginator.get_page(page_number)

    context = {
        'car_list': car_list,
        'myfilter': myfilter,

    }

    return render(request, 'car_list.html', context)


def car_detail(request, id):
    car_detail = Car.objects.get(id=id)

    context = {
        'car_detail': car_detail,
    }

    return render(request, 'car_detail.html', context)





def post_by_car_brand(request, brand):
    car_list = Car.objects.filter(brand__brand_name=brand)
    myfilter = CarFilter(request.GET, queryset=car_list)
    car_list = myfilter.qs

    paginator = Paginator(car_list, 8)
    page_number = request.GET.get('page')
    car_list = paginator.get_page(page_number)

    context = {
        'car_list': car_list,
        'myfilter': myfilter,

    }
    
    return render(request, 'car_list.html', context)


def car_form(request):
    car_list = Car.objects.all().order_by('-posted')
    myfilter = CarFilter(request.GET, queryset=car_list)
    car_list = myfilter.qs

    paginator = Paginator(car_list, 8)
    page_number = request.GET.get('page')
    car_list = paginator.get_page(page_number)
    
    if request.user.is_authenticated:
        cform = CarForm()

        if request.method == 'POST':
            cform = CarForm(request.POST, request.FILES)

            if cform.is_valid():
                obj = Car.objects.create(
                    user = User.objects.get(pk=request.user.id),
                    brand = cform.cleaned_data["brand"],
                    model_name = cform.cleaned_data["model_name"],
                    kms_driven = cform.cleaned_data["kms_driven"],
                    year = cform.cleaned_data["year"],
                    transmission = cform.cleaned_data["transmission"],
                    fuel_type = cform.cleaned_data["fuel_type"],
                    description = cform.cleaned_data["description"],
                    image = cform.cleaned_data.get("image"),
                    price = cform.cleaned_data["price"],
                    city = cform.cleaned_data["city"],
                    ownership = cform.cleaned_data["ownership"],
                    phone_number = cform.cleaned_data["phone_number"],
                )  
                obj.save()
                messages.info(request, 'Your Car ad has been successfully added.')

                context = {
                    'car_list': car_list,
                    'myfilter': myfilter,
                    
                }

                #return render(request, 'car_list.html', context)
                return redirect('cars:car_list')
                
        else:
            cform = CarForm()
        
        return render(request, 'car_form.html', {'cform': cform})
    
    messages.info(request, 'Login to post an ad!')
    return redirect('account_login')


def edit_car(request, pk):
    car=get_object_or_404(Car, id=pk)

    if request.user == car.user:
        cform = CarForm()

        if request.method == 'POST':
            cform = CarForm(request.POST, request.FILES, instance=car)

            if cform.is_valid():
                obj = cform.save(commit=False)
                obj.user = User.objects.get(pk=request.user.id)
                obj.save()
                messages.info(request, "Your car has been successfully edited!")

                return redirect('cars:car_list')
                
        else:
            cform = CarForm(instance=car)
        
        return render(request, 'edit_car.html', {'cform': cform})
        
    return redirect('account_login')


def delete_car(request, pk):
    car = get_object_or_404(Car, id=pk)

    if request.user == car.user:
        if request.method == 'POST':
            car.delete()
            return redirect('cars:car_list')
        
    context = {
        'car': car,
    }

    return render(request, 'car_delete_confirm.html', context)


def searchcars(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(model_name__icontains=query) | Q(description__icontains=query) | Q(city__icontains=query) 

            car_list = Car.objects.filter(lookups).distinct()
            
            paginator = Paginator(car_list, 8)
            page_number = request.GET.get('page')
            car_list = paginator.get_page(page_number)


            context = {
                'car_list': car_list,
                'submitbutton': submitbutton,
            }

            return render(request, 'car_list.html', context)

        else:
            return render(request, 'car_list.html')

    else:
        return render(request, 'car_list.html')



def post_by_fuel(request, fuel_type):
    car_list = Car.objects.filter(fuel_type__fuel_name=fuel_type)
    car_fuel = CarFuel.objects.all()
    car_ownership = CarOwnership.objects.all()
    car_transmission = CarTransmission.objects.all()

    paginator = Paginator(car_list, 8)
    page_number = request.GET.get('page')
    car_list = paginator.get_page(page_number)

    context = {
        'car_list': car_list,
        'car_fuel': car_fuel,
        'car_ownership': car_ownership,
        'car_transmission': car_transmission,

    }
    

    return render(request, 'car_list.html', context)


def post_by_ownership(request, ownership):
    car_list = Car.objects.filter(ownership__ownership_name=ownership)
    car_fuel = CarFuel.objects.all()
    car_ownership = CarOwnership.objects.all()
    car_transmission = CarTransmission.objects.all()

    paginator = Paginator(car_list, 8)
    page_number = request.GET.get('page')
    car_list = paginator.get_page(page_number)

    context = {
        'car_list': car_list,
        'car_fuel': car_fuel,
        'car_ownership': car_ownership,
        'car_transmission': car_transmission,

    }
    

    return render(request, 'car_list.html', context)


def post_by_transmission(request, transmission):
    car_list = Car.objects.filter(transmission__transmission_name=transmission)
    car_fuel = CarFuel.objects.all()
    car_ownership = CarOwnership.objects.all()
    car_transmission = CarTransmission.objects.all()

    paginator = Paginator(car_list, 8)
    page_number = request.GET.get('page')
    car_list = paginator.get_page(page_number)

    context = {
        'car_list': car_list,
        'car_fuel': car_fuel,
        'car_ownership': car_ownership,
        'car_transmission': car_transmission,

    }
    
    return render(request, 'car_list.html', context)


def low_to_high(request):
    car_list = Car.objects.all().order_by('price')
    car_fuel = CarFuel.objects.all()
    car_ownership = CarOwnership.objects.all()
    car_transmission = CarTransmission.objects.all()

    paginator = Paginator(car_list, 8)
    page_number = request.GET.get('page')
    car_list = paginator.get_page(page_number)

    context = {
        'car_list': car_list,
        'car_fuel': car_fuel,
        'car_ownership': car_ownership,
        'car_transmission': car_transmission,

    }

    return render(request, 'car_list.html', context)


def high_to_low(request):
    car_list = Car.objects.all().order_by('-price')
    car_fuel = CarFuel.objects.all()
    car_ownership = CarOwnership.objects.all()
    car_transmission = CarTransmission.objects.all()

    paginator = Paginator(car_list, 8)
    page_number = request.GET.get('page')
    car_list = paginator.get_page(page_number)

    context = {
        'car_list': car_list,
        'car_fuel': car_fuel,
        'car_ownership': car_ownership,
        'car_transmission': car_transmission,

    }

    return render(request, 'car_list.html', context)