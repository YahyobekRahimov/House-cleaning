from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, RegionViewSet, DistrictViewSet, VillageViewSet, UserViewSet, PositionViewSet, PhoneViewSet, LocationViewSet, MeasurmentViewSet, PricingViewSet, CategoryViewSet, ServiceViewSet, OrderViewSet, CommentViewSet, VisitViewSet, ServicePhotoViewSet, VisitPhotoViewSet, VideoViewSet, LinkViewSet, BranchPhoneViewSet, BranchViewSet

app_name = 'api'


router = DefaultRouter()
router.register('country', CountryViewSet, basename='countrie')
router.register('region', RegionViewSet, basename='region')
router.register('District', DistrictViewSet, basename='sistrict')
router.register('Village', VillageViewSet, basename='village')
router.register('User', UserViewSet, basename='user')
router.register('Position', PositionViewSet, basename='position')
router.register('Phone', PhoneViewSet, basename='phone')
router.register('Location', LocationViewSet, basename='location')
router.register('measurment', MeasurmentViewSet, basename='measurments')
router.register('Pricing', PricingViewSet, basename='pricing')
router.register('Categorie', CategoryViewSet, basename='categorie')
router.register('Service', ServiceViewSet, basename='srvice')
router.register('Order', OrderViewSet, basename='order')
router.register('Comment', CommentViewSet, basename='comment')
router.register('Visit', VisitViewSet, basename='visit')
router.register('ServicePhoto', ServicePhotoViewSet, basename='servicephoto')
router.register('VisitPhoto', VisitPhotoViewSet, basename='visitphoto')
router.register('Video', VideoViewSet, basename='video')
router.register('Link', LinkViewSet, basename='link')
router.register('BranchPhone', BranchPhoneViewSet, basename='branchphone')
router.register('Branche', BranchViewSet, basename='branch')



urlpatterns = [

]

urlpatterns += router.urls