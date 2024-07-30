from django.shortcuts import render, get_object_or_404,redirect
from .models import Car, BlogPost, Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CarSearchForm, ContactForm
from django.contrib import messages


def about_view(request):
    return render(request, 'about.html')


def blog_single_view(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    recent_posts = BlogPost.objects.exclude(id=post_id).order_by('-date_posted')[:3]
    return render(request, 'blog-single.html', {'post': post, 'recent_posts': recent_posts})


def car_view(request):
    cars = Car.objects.all().order_by('id')  # or any other field you want to order by
    for car in cars:
        print(f"Car: {car.name}, Image URL: {car.image.url}")
    form = CarSearchForm(request.GET)
    if form.is_valid():
        make = form.cleaned_data.get('make')
        model = form.cleaned_data.get('model')
        year = form.cleaned_data.get('year')
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')

        if make:
            cars = cars.filter(make__icontains=make)
        if model:
            cars = cars.filter(model__icontains=model)
        if year:
            cars = cars.filter(year=year)
        if price_min:
            cars = cars.filter(price__gte=price_min)
        if price_max:
            cars = cars.filter(price__lte=price_max)

    paginator = Paginator(cars, 9)  # Show 9 cars per page
    page = request.GET.get('page')
    cars = paginator.get_page(page)

    return render(request, 'car.html', {'cars': cars, 'form': form})

def car_single_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    print(f"Car: {car.name}, Image URL: {car.image.url}")
    related_cars = Car.objects.exclude(id=car_id)[:3]
    return render(request, 'car-single.html', {'car': car, 'related_cars': related_cars})
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def index_view(request):
    featured_cars = Car.objects.all()[:6]  # Get 6 featured cars
    return render(request, 'index.html', {'featured_cars': featured_cars})

def pricing_view(request):
    return render(request, 'pricing.html')

def services_view(request):
    return render(request, 'services.html')


def main_view(request):
    return render(request, 'main.html')