"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from main.admin import custom_admin_site
from main.views import about_view, blog_view, blog_single_view, car_view, car_single_view, contact_view, \
    index_view, main_view, pricing_view, services_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path('blog/', blog_view, name='blog'),
    path('blog-single/', blog_single_view, name='blog-single'),
    path('car/', car_view, name='car'),
    path('car/<int:car_id>/', car_single_view, name='car-single'),
    path('contact/', contact_view, name='contact'),
    path('', index_view, name='index'),
    path('main/', main_view, name='main'),
    path('pricing/', pricing_view, name='pricing'),
    path('services/', services_view, name='services'),
    path('admin/', custom_admin_site.urls),
    # other paths
]

