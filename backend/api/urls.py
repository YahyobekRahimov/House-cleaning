from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, RegionViewSet, DistrictViewSet, VillageViewSet, UserViewSet, PositionViewSet, PhoneViewSet, LocationViewSet, MeasurmentViewSet, PricingViewSet, CategoryViewSet, ServiceViewSet, OrderViewSet, CommentViewSet, VisitViewSet, ServicePhotoViewSet, VisitPhotoViewSet, VideoViewSet, LinkViewSet, BranchPhoneViewSet, BranchViewSet, EndpointViewSet

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

]

urlpatterns += router.urls
