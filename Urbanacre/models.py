from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# User table creation starts here
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, phone_number=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, phone_number=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, phone_number, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone_number']  # Specify the required fields here

    def __str__(self):
        return self.email
    
# User table ends here
    
# Realtor table creation starts here    
class Realtor(models.Model):
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='realtor')
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
    
# Realtor table creation ends here  


# Property table creation starts here
class Property(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'

    class PropertyType(models.TextChoices):
        RESIDENTIAL = 'Residential'
        COMMERCIAL = 'Commercial'    
    
    class Furnishing(models.TextChoices):
        FURNISH = 'Furnished'
        SEMIFURNISH = 'Semifurnished'
        UNFURNISH = 'Unfurnished'

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='listings')
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    society = models.TextField()
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    property_type = models.CharField(max_length=50, choices=PropertyType.choices, default=PropertyType.RESIDENTIAL)
    price = models.DecimalField(max_digits=100, decimal_places=5)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    balcony = models.IntegerField() 
    furnish_type = models.CharField(max_length=50, choices=Furnishing.choices, default=Furnishing.FURNISH)
    carpet_area = models.IntegerField()
    floor_no = models.CharField(max_length=20)
    facing = models.CharField(max_length=20)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title
    
# Property table creation starts here    
    
#  Contact table creation starts here       
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
# Contact table creation ends here        