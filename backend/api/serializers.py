from rest_framework import serializers
from core.models import Country, Region, District, Village, User, Position, Phone, Location, Measurment, Pricing, Category, Service, Order, Comment, Visit, ServicePhoto, VisitPhoto, Video, Link, BranchPhone, Branch

class CountrySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Country
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'country-detail'}
    }
class RegionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Region
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'region-detail'}
    }
class DistrictSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = District
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'district-detail'}
    }
class VillageSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Village
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'village-detail'}
    }
class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'user-detail'}
    }
class PositionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Position
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'position-detail'}
    }
class PhoneSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Phone
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'phone-detail'}
    }
class LocationSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Location
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'location-detail'}
    }
class MeasurmentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Measurment
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'measurment-detail'}
    }
class PricingSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Pricing
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'pricing-detail'}
    }
class CategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'category-detail'}
    }
class ServiceSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Service
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'service-detail'}
    }
class OrderSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Order
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'order-detail'}
    }
class CommentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'comment-detail'}
    }
class VisitSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Visit
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'visit-detail'}
    }
class ServicePhotoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ServicePhoto
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'servicephoto-detail'}
    }
class VisitPhotoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = VisitPhoto
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'visitphoto-detail'}
    }
class VideoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Video
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'video-detail'}
    }
class LinkSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Link
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'link-detail'}
    }
class BranchPhoneSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = BranchPhone
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'branchphone-detail'}
    }
class BranchSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Branch
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'branch-detail'}
    }