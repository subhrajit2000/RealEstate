from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm
from .models import Property, Realtor, Contact, CustomUser
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
    

@login_required
def addproperty(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the logged-in user
            user = CustomUser.objects.get(pk=request.user.pk)

            # Set the owner automatically to the logged-in user
            form.instance.owner = user

            # Generate a unique slug (consider using a slug generation library)
            # This is an example using a basic approach (replace with a robust method)
            base_slug = form.cleaned_data['title']
            count = 1
            slug = base_slug
            while Property.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            form.instance.slug = slug

            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'addproperty.html', {'form': form})