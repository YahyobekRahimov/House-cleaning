import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from api.models import Endpoint
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
#_________________________________________________________________________________
#_________________________________________________________________________ Country
class Country(models.Model):

    name = models.CharField(max_length=256, blank=False, null=True)
    # regions

    def clean(self):
        self.name = self.name.capitalize()
        return super().clean()
    
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "Countries"
    
#_________________________________________________________________________ Region
class Region(models.Model):

    name = models.CharField(max_length=64, blank=False, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, max_length=30, related_name='regions', null=True)
    # districts

    def clean(self):
        self.name = self.name.capitalize()
        return super().clean()
    
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.name

#_________________________________________________________________________ District
class District(models.Model):

    name = models.CharField(max_length=64, blank=False, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, max_length=30, related_name='districts', null=True) 
    # villages

    def clean(self):
        self.name = self.name.capitalize()
        return super().clean()
    
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.name

#_________________________________________________________________________ Village

class Village(models.Model):

    name = models.CharField(max_length=64, blank=False, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, max_length=30, related_name='villages', null=True)
    # services
    # users

    def clean(self):
        self.name = self.name.capitalize()
        return super().clean()
    
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.name

#_________________________________________________________________________ User
class User(AbstractUser):
    username = None
    email = models.EmailField(_('Email Address'), max_length=50, unique=True, null=True)
    email_is_verified = models.BooleanField(default=False, null=True)    
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='images/profile-pictures/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    village = models.ManyToManyField(Village, related_name='users', blank=True)
    # phones
    # positons
    # locations
    # comments
    # orders
    # contributions
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    def clean(self):
        if self.email:
            self.email = self.email.lower()
            
        if self.first_name:
            self.first_name = self.first_name.capitalize()
        
        if self.last_name:
            self.last_name = self.last_name.capitalize()
        super().clean()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='unique_email',
                fields=['email'],
            )
        ]
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.email
    
#_________________________________________________________________________ Position
class Position(models.Model):

    user = models.ForeignKey(User, related_name='positions', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False)

    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)


#_________________________________________________________________________ Phone
class Phone(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='phones')
    phone = PhoneNumberField()
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.phone
    

#_________________________________________________________________________ Location
class Location(models.Model):

    user = models.ForeignKey(User, blank=True, null=True, related_name='locations', on_delete=models.CASCADE)
    latitude = models.CharField(max_length=32, null=True)
    longitude = models.CharField(max_length=32, null=True)

    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.latitude + '-' + self.longitude

#_________________________________________________________________________ Measurment
class Measurment(models.Model):
    name = models.CharField(max_length=24, blank=False, null=True)

#_________________________________________________________________________ Pricing
class Pricing(models.Model):

    n = models.PositiveSmallIntegerField(null=True)
    measurment = models.ForeignKey(Measurment, related_name='pricings', on_delete=models.CASCADE)
    price = models.FloatField(null=True)
    # services
    
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.price + ' for '  + str(self.n)

#_________________________________________________________________________ Category
class Category(models.Model):

    name = models.CharField(max_length=255, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    # children
    # service
    # order
    info = models.TextField(blank=False)

    def clean(self):
        self.name = self.name.capitalize()
        return super().clean()
    
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Service Categories"

#_________________________________________________________________________ Service
class Service(models.Model):

    name = models.CharField(max_length=256, blank=False, null=True)
    category = models.ManyToManyField(Category, related_name='services',)
    info = models.TextField(blank=False, null=True)
    villages = models.ManyToManyField(Village, related_name='services')
    price = models.FloatField(null=True)
    pricing = models.ManyToManyField(Pricing, related_name='services', blank=False)
    # clients
    # orders
    # photos
    since_date = models.DateField(blank=False, null=True)
    def clean(self):
        self.name = self.name.capitalize()
        return super().clean()
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.name} (since {self.since_date})'

#_________________________________________________________________________ Order
class Order(models.Model):

    service = models.ForeignKey(Service, related_name='orders', on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=16, choices=(('pending', 'pending'), ('process', 'process'), ('done', 'done'), ('rejected', 'rejected')), blank=False, null=True)
    time_ordered = models.DateTimeField(blank=True, null=True)
    service_name = models.CharField(max_length=64, blank=True, null=True)
    client_name = models.CharField(max_length=64, blank=True, null=True)
    # visits
    # comments

    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)().save(*args, **kwargs)

    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return f"{self.client_name}: {self.service_name} - {self.status}"

#_________________________________________________________________________ Comment
class Comment(models.Model):

    GRADES = (
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
        ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', blank=False, null=True)
    grade = models.CharField(max_length=2, choices=GRADES, blank=False, null=True)
    reason = models.TextField(blank=False, null=True)
    date = models.DateTimeField(auto_created=True, null=True)
    order = models.ForeignKey(Order, related_name='comments', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.reason[:50]

#_________________________________________________________________________ Visit
class Visit(models.Model):

    started = models.DateTimeField(blank=True, null=True)
    finished = models.DateTimeField(blank=True, null=True)
    # photos
    contributors = models.ManyToManyField(User, related_name='contributions')
    info = models.TextField(blank=True, null=True)
    order = models.ForeignKey(Order, related_name='visits', on_delete=models.CASCADE)
    
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return f'{self.started}-{self.finished}'



#_________________________________________________________________________ Service Photo
class ServicePhoto(models.Model):

    photo = models.ImageField(upload_to='images/services', null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, related_name='photos')
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self):
        return f"(photo) {self.service.name}"

#_________________________________________________________________________ Visit Photo
class VisitPhoto(models.Model):

    photo = models.ImageField(upload_to='images/visits', null=True)
    visit = models.ForeignKey(Visit, related_name='photos', on_delete=models.CASCADE)

    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self):
        return f"(photo) {self.visit}"

#_________________________________________________________________________ Video
class Video(models.Model):

    name = models.CharField(max_length=256)
    url = models.URLField(blank=False, null=True)

    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.name + " Video"

#_________________________________________________________________________ Company

class Link(models.Model):

    link = models.URLField(blank=False, null=True)
    name = models.CharField(max_length=32, blank=False, null=True)
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return f'{self.name}'
class BranchPhone(models.Model):

    phone = PhoneNumberField(blank=False, null=True, default='7757')
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return f'{self.phone}'
    
class Branch(models.Model):
    key = models.CharField(max_length=32, blank=False, null=True)
    name = models.CharField(max_length=512, blank=False, null=True)
    shortPhone = models.CharField(max_length=6, blank=True)
    work_time_start = models.CharField(max_length=5, blank=False, null=True)
    work_time_end = models.CharField(max_length=5, blank=False, null=True)

    phones = models.ManyToManyField(BranchPhone, related_name='branches', blank=True)
    links = models.ManyToManyField(Link, related_name='branches', blank=True)
    
    
    def save(self, *args, **kwargs):
        endpoint = Endpoint.objects.get(name='contact')
        endpoint.key = str(uuid.uuid4().int)[:10]
        endpoint.save()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.key} ({self.name})'

