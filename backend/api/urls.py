from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, RegionViewSet, DistrictViewSet, VillageViewSet, UserViewSet, PositionViewSet, PhoneViewSet, LocationViewSet, MeasurmentViewSet, PricingViewSet, CategoryViewSet, ServiceViewSet, OrderViewSet, CommentViewSet, VisitViewSet, ServicePhotoViewSet, VisitPhotoViewSet, VideoViewSet, LinkViewSet, BranchPhoneViewSet, BranchViewSet, EndpointViewSet


from .views import isnew_country, isnew_region, isnew_district, isnew_village, isnew_user, isnew_position, isnew_phone, isnew_location, isnew_measurment, isnew_pricing, isnew_category, isnew_service, isnew_order, isnew_comment, isnew_visit, isnew_servicephoto, isnew_visitphoto, isnew_video, isnew_link, isnew_branchphone, isnew_branch, isnew_endpoint
app_name = 'api'


router = DefaultRouter()
router.register('country', CountryViewSet, basename='country')
router.register('region', RegionViewSet, basename='region')
router.register('district', DistrictViewSet, basename='district')
router.register('village', VillageViewSet, basename='village')
router.register('user', UserViewSet, basename='user')
router.register('position', PositionViewSet, basename='position')
router.register('phone', PhoneViewSet, basename='phone')
router.register('location', LocationViewSet, basename='location')
router.register('measurment', MeasurmentViewSet, basename='measurment')
router.register('pricing', PricingViewSet, basename='pricing')
router.register('category', CategoryViewSet, basename='category')
router.register('srvice', ServiceViewSet, basename='srvice')
router.register('order', OrderViewSet, basename='order')
router.register('comment', CommentViewSet, basename='comment')
router.register('visit', VisitViewSet, basename='visit')
router.register('servicephoto', ServicePhotoViewSet, basename='servicephoto')
router.register('visitphoto', VisitPhotoViewSet, basename='visitphoto')
router.register('video', VideoViewSet, basename='video')
router.register('link', LinkViewSet, basename='link')
router.register('branchphone', BranchPhoneViewSet, basename='branchphone')
router.register('branch', BranchViewSet, basename='branch')
router.register('endpoint', EndpointViewSet, basename='endpoint')


urlpatterns = [
  path("isnew/country/<str:key>", isnew_country, name='isnew_country'),
  path("isnew/region/<str:key>", isnew_region, name='isnew_region'),
  path("isnew/district/<str:key>", isnew_district, name='isnew_district'),
  path("isnew/village/<str:key>", isnew_village, name='isnew_village'),
  path("isnew/user/<str:key>", isnew_user, name='isnew_user'),
  path("isnew/position/<str:key>", isnew_position, name='isnew_position'),
  path("isnew/phone/<str:key>", isnew_phone, name='isnew_phone'),
  path("isnew/location/<str:key>", isnew_location, name='isnew_location'),
  path("isnew/measurment/<str:key>", isnew_measurment, name='isnew_measurment'),
  path("isnew/pricing/<str:key>", isnew_pricing, name='isnew_pricing'),
  path("isnew/category/<str:key>", isnew_category, name='isnew_category'),
  path("isnew/service/<str:key>", isnew_service, name='isnew_service'),
  path("isnew/order/<str:key>", isnew_order, name='isnew_order'),
  path("isnew/comment/<str:key>", isnew_comment, name='isnew_comment'),
  path("isnew/visit/<str:key>", isnew_visit, name='isnew_visit'),
  path("isnew/servicephoto/<str:key>", isnew_servicephoto, name='isnew_servicephoto'),
  path("isnew/visitphoto/<str:key>", isnew_visitphoto, name='isnew_visitphoto'),
  path("isnew/video/<str:key>", isnew_video, name='isnew_video'),
  path("isnew/link/<str:key>", isnew_link, name='isnew_link'),
  path("isnew/branchphone/<str:key>", isnew_branchphone, name='isnew_branchphone'),
  path("isnew/branch/<str:key>", isnew_branch, name='isnew_branch'),
  path("isnew/endpoint/<str:key>", isnew_endpoint, name='isnew_endpoint'),
]

urlpatterns += router.urls
