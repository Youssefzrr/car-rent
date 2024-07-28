from django.contrib import admin
from .models import Contact, Visitor
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

custom_admin_site = CustomAdminSite(name='customadmin')
custom_admin_site.register(Contact, ContactAdmin)
custom_admin_site.register(Visitor, VisitorAdmin)