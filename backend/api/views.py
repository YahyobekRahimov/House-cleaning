from django.shortcuts import render
from .models import Endpoint
from rest_framework.decorators import api_view
from rest_framework import viewsets
from core.models import Country, Region, District, Village, User, Position, Phone, Location, Measurment, Pricing, Category, Service, Order, Comment, Visit, ServicePhoto, VisitPhoto, Video, Link, BranchPhone, Branch
from .serializers import CountrySerializer, RegionSerializer, DistrictSerializer, VillageSerializer, UserSerializer, PositionSerializer, PhoneSerializer, LocationSerializer, MeasurmentSerializer, PricingSerializer, CategorySerializer, ServiceSerializer, OrderSerializer, CommentSerializer, VisitSerializer, ServicePhotoSerializer, VisitPhotoSerializer, VideoSerializer, LinkSerializer, BranchPhoneSerializer, BranchSerializer, EndpointSerializer

from django.http import JsonResponse

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class MeasurmentViewSet(viewsets.ModelViewSet):
    queryset = Measurment.objects.all()
    serializer_class = MeasurmentSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class PricingViewSet(viewsets.ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class ServicePhotoViewSet(viewsets.ModelViewSet):
    queryset = ServicePhoto.objects.all()
    serializer_class = ServicePhotoSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class VisitPhotoViewSet(viewsets.ModelViewSet):
    queryset = VisitPhoto.objects.all()
    serializer_class = VisitPhotoSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class BranchPhoneViewSet(viewsets.ModelViewSet):
    queryset = BranchPhone.objects.all()
    serializer_class = BranchPhoneSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete'] 

class EndpointViewSet(viewsets.ModelViewSet):
    queryset = Endpoint.objects.all()
    serializer_class = EndpointSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete'] 

# _______________________________________________________________________________
def isnew_country(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.country == key})
    
def isnew_region(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.region == key})
    
def isnew_district(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.district == key})
    
def isnew_village(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.village == key})
    
def isnew_user(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.user == key})
    
def isnew_position(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.position == key})
    
def isnew_phone(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.phone == key})
    
def isnew_location(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.location == key})
    
def isnew_measurment(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.measurment == key})
    
def isnew_pricing(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.pricing == key})
    
def isnew_category(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.category == key})
    
def isnew_service(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.service == key})
    
def isnew_order(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.order == key})
    
def isnew_comment(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.comment == key})
    
def isnew_visit(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.visit == key})
    
def isnew_servicephoto(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.servicephoto == key})
    
def isnew_visitphoto(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.visitphoto == key})
    
def isnew_video(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.video == key})
    
def isnew_link(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.link == key})
    
def isnew_branchphone(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.branchphone == key})
    
def isnew_branch(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.branch == key})
    
def isnew_endpoint(request, key):
    model = Endpoint.objects.first()
    return JsonResponse({'new': model.endpoint == key})
    


