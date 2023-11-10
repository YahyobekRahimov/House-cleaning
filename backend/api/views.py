from django.shortcuts import render
from .models import Endpoint
from rest_framework.decorators import api_view
from rest_framework import viewsets
from core.models import Country, Region, District, Village, User, Position, Phone, Location, Measurment, Pricing, Category, Service, Order, Comment, Visit, ServicePhoto, VisitPhoto, Video, Link, BranchPhone, Branch
from .serializers import CountrySerializer, RegionSerializer, DistrictSerializer, VillageSerializer, UserSerializer, PositionSerializer, PhoneSerializer, LocationSerializer, MeasurmentSerializer, PricingSerializer, CategorySerializer, ServiceSerializer, OrderSerializer, CommentSerializer, VisitSerializer, ServicePhotoSerializer, VisitPhotoSerializer, VideoSerializer, LinkSerializer, BranchPhoneSerializer, BranchSerializer

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
    lookup_field = 'id'
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







from rest_framework.response import Response
from .serializers import BranchSerializer
from core import models as m
from django.http import HttpResponse, JsonResponse
# @api_view(['GET', 'POST'])
def contact(request, key):
    if request.method == 'POST':
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            # Process the validated data
            # Access the validated data using serializer.validated_data
            return Response(serializer.validated_data, status=201)
        else:
            return Response(serializer.errors, status=400)
    if key:
        endpoint = Endpoint.objects.get(name='contact')
        return JsonResponse({'old': key==endpoint.key})

    branch = m.Branch.objects.all()
    serializer = BranchSerializer(branch, many=True)
    serialized_data = serializer.data
    return Response(serialized_data)
