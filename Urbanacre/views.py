from django.shortcuts import render
from .models import Property, Realtor

def index(request):
    option = request.GET.get('option', 'featured')  # Get the option from the request URL
    if option == 'featured':
        properties = Property.objects.order_by('?')[:6]  # Retrieve random properties for featured section
    elif option == 'sale':
        properties = Property.objects.filter(sale_type='For Sale').order_by('?')[:6]  # Retrieve random properties for sale
    elif option == 'rent':
        properties = Property.objects.filter(sale_type='For Rent').order_by('?')[:6]  # Retrieve random properties for rent
    else:
        properties = Property.objects.order_by('?')[:6]  # Default to featured properties
    realtors = Realtor.objects.all().order_by('name')  # Get all realtors sorted by name    
    return render(request, "index.html", {'properties': properties, 'realtors': realtors})


def about(request):
    realtors = Realtor.objects.all().order_by('name')  # Get all realtors sorted by name
    return render(request, "about.html", {'realtors': realtors})


def contact(request):
    pass