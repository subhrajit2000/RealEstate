from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Property, Realtor, Contact

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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save data to Contact model
        contact = Contact.objects.create(
            name= name,
            email= email,
            subject= subject,
            message= message
        )
        messages.success(request, "Message send successfully!")
        return redirect('contact')
    else:
        return render(request, 'contact.html')
    

def property_list(request):
    option = request.GET.get('option', 'featured')  # Get the option from the request URL
    if option == 'featured':
        properties = Property.objects.order_by('?')[:6]  # Retrieve random properties for featured section
    elif option == 'sale':
        properties = Property.objects.filter(sale_type='For Sale').order_by('?')[:6]  # Retrieve random properties for sale
    elif option == 'rent':
        properties = Property.objects.filter(sale_type='For Rent').order_by('?')[:6]  # Retrieve random properties for rent
    else:
        properties = Property.objects.order_by('?')[:6]  # Default to featured properties

    return render(request, "property_list.html", {'properties': properties})