from django.urls import path
from core import views
from django.contrib.auth import views as auth_views
from core import views as v




app_name = 'core'



urlpatterns = [
    path('', views.home, name='home'),
    # ... other URL patterns ...
    path('signup/', v.signup_view, name='signup'),
    path('verify-email/', v.verify_email, name='verify-email'),
    path('verify-email/done/', v.verify_email_done, name='verify-email-done'),
    path('verify-email-confirm/<uidb64>/<token>/', v.verify_email_confirm, name='verify-email-confirm'),
    path('verify-email/complete/', v.verify_email_complete, name='verify-email-complete'),    
] + [
  path('api/branch', v.branch, name='branch-api'),
  path('api/brach/is_new/<key:str>', v.branch_is_new, name='branch-api-is_new')
]

