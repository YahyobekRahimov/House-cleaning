from rest_framework import serializers
from core.models import Country, Region, District, Village, User, Position, Phone, Location, Measurment, Pricing, Category, Service, Order, Comment, Visit, ServicePhoto, VisitPhoto, Video, Link, BranchPhone, Branch
from .models import Endpoint

class CountrySerializer(serializers.ModelSerializer):
  class Meta:
    model = Country
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'country-detail'}
    }
class RegionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Region
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'region-detail'}
    }
class DistrictSerializer(serializers.ModelSerializer):
  class Meta:
    model = District
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'district-detail'}
    }
class VillageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Village
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'village-detail'}
    }
class UserSerializer(serializers.ModelSerializer):
  village = VillageSerializer(many=True)
  class Meta:
    model = User
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'user-detail'}
    }
class PositionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Position
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'position-detail'}
    }
class PhoneSerializer(serializers.ModelSerializer):
  class Meta:
    model = Phone
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'phone-detail'}
    }
class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'location-detail'}
    }
class MeasurmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Measurment
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'measurment-detail'}
    }
class PricingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pricing
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'pricing-detail'}
    }
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'category-detail'}
    }
class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Service
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'service-detail'}
    }
class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'order-detail'}
    }
class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'comment-detail'}
    }
class VisitSerializer(serializers.ModelSerializer):
  class Meta:
    model = Visit
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'visit-detail'}
    }
class ServicePhotoSerializer(serializers.ModelSerializer):
  class Meta:
    model = ServicePhoto
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'servicephoto-detail'}
    }
class VisitPhotoSerializer(serializers.ModelSerializer):
  class Meta:
    model = VisitPhoto
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'visitphoto-detail'}
    }
class VideoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Video
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'video-detail'}
    }
class LinkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Link
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'link-detail'}
    }
class BranchPhoneSerializer(serializers.ModelSerializer):
  class Meta:
    model = BranchPhone
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'branchphone-detail'}
    }
class BranchSerializer(serializers.ModelSerializer):
  class Meta:
    model = Branch
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'branch-detail'}
    }

class EndpointSerializer(serializers.ModelSerializer):
  class Meta:
    model = Endpoint
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'endpoint-detail'}
    }

  