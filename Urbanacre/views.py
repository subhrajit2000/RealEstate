from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Property, Realtor, Contact
from django.core.paginator import Paginator

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
    PropertyData = Property.objects.all() # collects property data from the database
    paginator = Paginator(PropertyData, 6) # 6 refers to the no. of data want to show in a page
    page_number = request.GET.get('page') # 
    PropertyDatafinal = paginator.get_page(page_number)
    totalpage = PropertyDatafinal.paginator.num_pages

    Saleproperty = Property.objects.filter(sale_type='For Sale').order_by('?')[:6]

    data = {
        'propertyData': PropertyDatafinal,
        'saleproperties': Saleproperty,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }

    return render(request, "property_list.html", data)

def property_details(request, slug):
        property = get_object_or_404(Property, slug=slug)
        return render(request, 'property_details.html', {'property': property})
    

def addproperty(request):
    if not request.user.is_authenticated:
        error_message = "You need to be logged in to access this functionality."
        return render(request, 'add_property.html', {'error_message': error_message})
    else:
        if request.method == 'POST':
            realtor_id = request.POST.get('realtor_id')
            owner_id = request.POST.get('owner_id')
            slug = request.POST.get('slug')
            title = request.POST.get('title')
            location = request.POST.get('location')
            description = request.POST.get('description')
            society = request.POST.get('society')
            sale_type = request.POST.get('sale_type')
            property_type = request.POST.get('property_type')
            price = request.POST.get('price')
            bedrooms = request.POST.get('bedrooms')
            bathrooms = request.POST.get('bathrooms')
            balcony = request.POST.get('balcony')
            furnish_type = request.POST.get('furnish_type')
            carpet_area = request.POST.get('carpet_area')
            floor_no = request.POST.get('floor_no')
            facing = request.POST.get('facing')
            photo_main = request.FILES.get('photo_main')
            photo_1 = request.FILES.get('photo_1')
            photo_2 = request.FILES.get('photo_2')
            photo_3 = request.FILES.get('photo_3')
            photo_4 = request.FILES.get('photo_4')
            photo_5 = request.FILES.get('photo_5')
            photo_6 = request.FILES.get('photo_6')
            photo_7 = request.FILES.get('photo_7')
            photo_8 = request.FILES.get('photo_8')
            photo_9 = request.FILES.get('photo_9')
            photo_10 = request.FILES.get('photo_10')
            is_published = request.POST.get('is_published')

            Property.objects.create(
                realtor_id=realtor_id,
                owner_id=owner_id,
                slug=slug,
                title=title,
                location=location,
                description=description,
                society=society,
                sale_type=sale_type,
                property_type=property_type,
                price=price,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                balcony=balcony,
                furnish_type=furnish_type,
                carpet_area=carpet_area,
                floor_no=floor_no,
                facing=facing,
                photo_main=photo_main,
                photo_1=photo_1,
                photo_2=photo_2,
                photo_3=photo_3,
                photo_4=photo_4,
                photo_5=photo_5,
                photo_6=photo_6,
                photo_7=photo_7,
                photo_8=photo_8,
                photo_9=photo_9,
                photo_10=photo_10,
                is_published=is_published
            )
            messages.success(request, 'Property added successfully!')
            return redirect('property_list')  # Redirect to a view displaying the list of properties

        
        return render(request, 'addproperty.html')
    
