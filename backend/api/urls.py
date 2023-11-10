from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, RegionViewSet, DistrictViewSet, VillageViewSet, UserViewSet, PositionViewSet, PhoneViewSet, LocationViewSet, MeasurmentViewSet, PricingViewSet, CategoryViewSet, ServiceViewSet, OrderViewSet, CommentViewSet, VisitViewSet, ServicePhotoViewSet, VisitPhotoViewSet, VideoViewSet, LinkViewSet, BranchPhoneViewSet, BranchViewSet

app_name = 'api'


router = DefaultRouter()
router.register('Countries', CountryViewSet, basename='Countries')
router.register('Regions', RegionViewSet, basename='Regions')
router.register('Districts', DistrictViewSet, basename='Districts')
router.register('Villages', VillageViewSet, basename='Villages')
router.register('Users', UserViewSet, basename='Users')
router.register('Positions', PositionViewSet, basename='Positions')
router.register('Phones', PhoneViewSet, basename='Phones')
router.register('Locations', LocationViewSet, basename='Locations')
router.register('Measurments', MeasurmentViewSet, basename='Measurments')
router.register('Pricings', PricingViewSet, basename='Pricings')
router.register('Categories', CategoryViewSet, basename='Categories')
router.register('Services', ServiceViewSet, basename='Services')
router.register('Orders', OrderViewSet, basename='Orders')
router.register('Comments', CommentViewSet, basename='Comments')
router.register('Visits', VisitViewSet, basename='Visits')
router.register('ServicePhotos', ServicePhotoViewSet, basename='ServicePhotos')
router.register('VisitPhotos', VisitPhotoViewSet, basename='VisitPhotos')
router.register('Videos', VideoViewSet, basename='Videos')
router.register('Links', LinkViewSet, basename='Links')
router.register('BranchPhones', BranchPhoneViewSet, basename='BranchPhones')
router.register('Branches', BranchViewSet, basename='Branches')



urlpatterns = [

]

urlpatterns += router.urls