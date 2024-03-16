from django.shortcuts import render
from .models import Property
# Create your views here.
def index(request):
    prop = Property.objects.first()
    return render(request, "index.html", {'prop':prop})
