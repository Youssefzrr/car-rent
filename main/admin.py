from django.contrib import admin
from .models import Contact, Visitor,Car
from django.urls import path
from django.shortcuts import render

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent')
    list_filter = ('date_sent',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('date_sent',)

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'user_agent', 'visit_time')
    list_filter = ('visit_time',)
    search_fields = ('ip_address', 'user_agent')

class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        context = {
            'contact_count': Contact.objects.count(),
            'visitor_count': Visitor.objects.count(),
            # Add more context data as needed
        }
        return render(request, 'admin/dashboard.html', context)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'transmission', 'fuel')
    list_filter = ('brand', 'transmission', 'fuel')
    search_fields = ('name', 'brand')
    readonly_fields = ('id',)
    fieldsets = (
        (None, {
            'fields': ('name', 'brand', 'price', 'image')
        }),
        ('Specifications', {
            'fields': ('mileage', 'transmission', 'seats', 'luggage', 'fuel')
        }),
    )

# If you prefer a simpler registration without customization, you can use:
# admin.site.register(Car)


custom_admin_site = CustomAdminSite(name='customadmin')
custom_admin_site.register(Contact, ContactAdmin)
custom_admin_site.register(Visitor, VisitorAdmin)
