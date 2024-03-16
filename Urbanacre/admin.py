from django.contrib import admin
from .models import CustomUser, Realtor, Property, Contact

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone_number', 'is_active', 'is_staff')
    search_fields = ('email', 'name', 'phone_number')
    list_filter = ('is_active', 'is_staff')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone_number', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'top_seller', 'date_hired')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('top_seller', 'date_hired')
    ordering = ('name',)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'realtor', 'location', 'price', 'list_date', 'is_published')
    list_filter = ('realtor', 'list_date', 'is_published')
    search_fields = ('title', 'location', 'description')
    readonly_fields = ('list_date',)
    ordering = ('-list_date',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'subject', 'contact_date')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('contact_date',)
    ordering = ('-contact_date',)

