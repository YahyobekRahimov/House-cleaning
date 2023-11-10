from django.urls import path

from .views import (
    signup_view, 
    activate_account,
    login_view,
    logout_view,
    password_reset_view,
    password_reset_confirm
)

app_name = 'accaunts'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('activate/<uidb64>/<token>/', activate_account, name='activate'), 
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password-reset/', password_reset_view, name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
]
