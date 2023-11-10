from rest_framework import serializers
from core.models import Country, Region, District, Village, User, Position, Phone, Location, Measurment, Pricing, Category, Service, Order, Comment, Visit, ServicePhoto, VisitPhoto, Video, Link, BranchPhone, Branch

class CountrySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Country
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Country-detail'}
    }
class RegionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Region
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Region-detail'}
    }
class DistrictSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = District
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'District-detail'}
    }
class VillageSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Village
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Village-detail'}
    }
class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'User-detail'}
    }
class PositionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Position
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Position-detail'}
    }
class PhoneSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Phone
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Phone-detail'}
    }
class LocationSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Location
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Location-detail'}
    }
class MeasurmentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Measurment
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Measurment-detail'}
    }
class PricingSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Pricing
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Pricing-detail'}
    }
class CategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Category-detail'}
    }
class ServiceSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Service
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Service-detail'}
    }
class OrderSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Order
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Order-detail'}
    }
class CommentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Comment-detail'}
    }
class VisitSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Visit
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Visit-detail'}
    }
class ServicePhotoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ServicePhoto
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'ServicePhoto-detail'}
    }
class VisitPhotoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = VisitPhoto
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'VisitPhoto-detail'}
    }
class VideoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Video
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Video-detail'}
    }
class LinkSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Link
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Link-detail'}
    }
class BranchPhoneSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = BranchPhone
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'BranchPhone-detail'}
    }
class BranchSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Branch
    fields = '__all__'
    extra_kwargs = {
      'url': {'view_name': 'Branch-detail'}
    }