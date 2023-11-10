from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import Country, Region, District, Village, User, Position, Phone, Location, Measurment, Pricing, Category, Service, Order, Comment, Visit, ServicePhoto, VisitPhoto, Video, Link, BranchPhone, Branch
# Register your models here.

# class CustomUserAdmin(BaseUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal Info', {'fields': ('profile_photo', 'bio')}),
#         ('Permissions', {'fields': ('village',)}),
#     )
#     list_display = ('email', 'profile_photo', 'bio')
#     search_fields = ('email', 'profile_photo', 'bio')

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Village)
admin.site.register(Position)
admin.site.register(Phone)
admin.site.register(Location)
admin.site.register(Measurment)
admin.site.register(Pricing)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Visit)
admin.site.register(ServicePhoto)
admin.site.register(VisitPhoto)
admin.site.register(Video)
admin.site.register(Link)
admin.site.register(BranchPhone)
admin.site.register(Branch)
