from re import template
from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from . forms import BikeForm
from django.contrib.auth.models import User
from . models import Bike, Brands, Ownership
from cars.models import Car
from cars.models import CarBrand
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import resolve
from django.http import HttpResponse
from django.template import loader
from .filters import BikeFilter
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def bike_detail(request, id):
    bike_detail = Bike.objects.get(id=id)

    context = {
        'bike_detail' : bike_detail,
    }

    return render(request, 'bike_detail.html', context)


def bike_list(request):
    bike_list = Bike.objects.all().order_by('-posted')

    # search
    search_query1 = request.GET.get('b')
    if search_query1:
        bike_list = bike_list.filter(
            Q(description__icontains=search_query1) |
            Q(model_name__icontains=search_query1) 
        )
    
    myfilter = BikeFilter(request.GET, queryset=bike_list)
    bike_list = myfilter.qs

    
    paginator = Paginator(bike_list, 8)
    page_number = request.GET.get('page')
    bike_list = paginator.get_page(page_number)

    context = {
        'bike_list': bike_list,
        'myfilter': myfilter,
    }

    return render(request, 'bike_list.html', context)


def bike_form(request):
    bike_list = Bike.objects.all().order_by('-posted')

    myfilter = BikeFilter(request.GET, queryset=bike_list)
    bike_list = myfilter.qs
    
    paginator = Paginator(bike_list, 8)
    page_number = request.GET.get('page')
    bike_list = paginator.get_page(page_number)

    if request.user.is_authenticated:
        bform = BikeForm()

        if request.method == 'POST':
            bform = BikeForm(request.POST, request.FILES)

            if bform.is_valid():
                obj = Bike.objects.create(
                    user = User.objects.get(pk=request.user.id),
                    brand = bform.cleaned_data["brand"],
                    model_name = bform.cleaned_data["model_name"],
                    kms_driven = bform.cleaned_data["kms_driven"],
                    year = bform.cleaned_data["year"],
                    description = bform.cleaned_data["description"],
                    image = bform.cleaned_data.get("image"),
                    price = bform.cleaned_data["price"],
                    city = bform.cleaned_data["city"],
                    ownership = bform.cleaned_data["ownership"],
                    phone_number = bform.cleaned_data["phone_number"],
                )  
                obj.save()
                messages.info(request, 'Your Bike ad has been successfully posted.')

                context = {
                    'bike_list': bike_list,
                    'myfilter': myfilter,
                }

                #return render(request, 'bike_list.html', context)
                return redirect('bikes:bike_list')
                
        else:
            bform = BikeForm()
        
        return render(request, 'bike_form.html', {'bform': bform})
    
    messages.info(request, 'Login to post an ad!')
    return redirect('account_login')



def edit_bike(request, pk):
    bike=get_object_or_404(Bike, id=pk)

    if request.user == bike.user:
        bform = BikeForm()

        if request.method == 'POST':
            bform = BikeForm(request.POST, request.FILES, instance=bike)

            if bform.is_valid():
                obj = bform.save(commit=False)
                obj.user = User.objects.get(pk=request.user.id)
                obj.save()
                messages.info(request, 'Your bike has been successfully edited.')

                return redirect('bikes:bike_list')
                
        else:
            bform = BikeForm(instance=bike)
        
        return render(request, 'edit_bike.html', {'bform': bform})
        
    return redirect('account_login')


def delete_bike(request, pk):
    bike = get_object_or_404(Bike, id=pk)

    if request.user == bike.user:
        if request.method == 'POST':
            bike.delete()
            return redirect('bikes:bike_list')
        
    context = {
        'bike': bike,
    }

    return render(request, 'bike_delete_confirm.html', context)
    

'''def brands(request):
    all_brands = Brands.objects.all().order_by('-id')
    car_brands = CarBrand.objects.all()

    context = {
        'all_brands': all_brands,
        'car_brands': car_brands,
        }
    
    return render(request, 'brands.html', context)'''


def searchposts(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(model_name__icontains=query) | Q(description__icontains=query) | Q(city__icontains=query) 

            bike_list = Bike.objects.filter(lookups).distinct()


            context = {
                'bike_list': bike_list,
                'submitbutton': submitbutton,
            }

            return render(request, 'bike_list.html', context)

        else:
            return render(request, 'bike_list.html')

    else:
        return render(request, 'bike_list.html')



def post_by_brand(request, brand):
    bike_list = Bike.objects.filter(brand__brand_name=brand)
    all_brands = Brands.objects.all()

    myfilter = BikeFilter(request.GET, queryset=bike_list)

    paginator = Paginator(bike_list, 8)
    page_number = request.GET.get('page')
    bike_list = paginator.get_page(page_number)


    context = {
        'bike_list': bike_list,
        'all_brands': all_brands,
        'myfilter': myfilter,
    }

    return render(request, 'bike_list.html', context)


def low_to_high(request):
    bike_list = Bike.objects.all().order_by('price')

    paginator = Paginator(bike_list, 8)
    page_number = request.GET.get('page')
    bike_list = paginator.get_page(page_number)

    context = {
        'bike_list': bike_list,

    }

    return render(request, 'bike_list.html', context)


def high_to_low(request):
    bike_list = Bike.objects.all().order_by('-price')

    paginator = Paginator(bike_list, 8)
    page_number = request.GET.get('page')
    bike_list = paginator.get_page(page_number)

    context = {
        'bike_list': bike_list,

    }

    return render(request, 'bike_list.html', context)


'''def post_by_ownership(request, ownership):
    bike_list = Bike.objects.filter(ownership__ownership=ownership)
    ownerships = Ownership.objects.all()

    paginator = Paginator(bike_list, 8)
    page_number = request.GET.get('page')
    bike_list = paginator.get_page(page_number)

    context = {
        'bike_list': bike_list,
        'ownerships': ownerships,
    }

    return render(request, 'bike_list.html', context)'''


def user_vehicle_list(request, username):
    user = get_object_or_404(User, username=username)
    bike_list = Bike.objects.filter(user=user).order_by('-posted')
    car_list = Car.objects.filter(user=user).order_by('-posted')

    context = {
        'user': user,
        'bike_list': bike_list,
        'car_list': car_list,
    }

    return render(request, 'user_vehicle_list.html', context)


def user_bike_list(request, username):
    user1 = get_object_or_404(User, username=username)
    url_name = resolve(request.path).url_name

    if url_name == 'user_bike_list':
	    user_bike_list = Bike.objects.filter(user=user1).order_by('-posted')
    else:
	    user_bike_list = Car.objects.filter(user=user1).order_by('-posted')

    template = loader.get_template('user_bike_list.html')

    context = {
        'url_name': url_name,
        'user_bike_list': user_bike_list,
        'user1': user1

    }

    return HttpResponse(template.render(context, request))


def brands_new(request):
    url_name = resolve(request.path).url_name

    bike_list = Bike.objects.all().order_by('-posted')
    myfilter = BikeFilter(request.GET, queryset=bike_list)
    bike_list = myfilter.qs

    if url_name == 'brands_new':
        bike_brands = CarBrand.objects.all()
    else:
        bike_brands = Brands.objects.all()

    template = loader.get_template('brand.html')

    context = {
        'bike_brands': bike_brands,
        'url_name': url_name,
        'myfilter': myfilter,
    }

    return HttpResponse(template.render(context, request))


def sendEmail(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
        messages.info(request, f'Email sent Successfully to {email}')
        #return render(request, 'email_sent.html', {'email': email})

    return render(request, 'sendEmail.html')