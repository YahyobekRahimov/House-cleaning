from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
import random

from core import models as m

def generate_random_number():
    return random.randint(100000, 999999)

def send_authorization_email(email, random_number):
    subject = 'Authorization Code'
    message = f'Your authorization code is: {random_number}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def home(request):
    send_authorization_email('niddihur@gmail.com', generate_random_number())
    return HttpResponse('Home')


from .forms import UserRegisterForm
from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render

def signup_view(request):
    if request.method == "POST":
        next = request.GET.get('next')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(email=user.email, password=password)
            login(request, new_user)
            if next:
                return redirect(next)
            else:
                return redirect('core:verify-email')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/signup.html', context)

# Add below existing imports
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages

# so we can reference the user model as User instead of CustomUser
User = get_user_model()

# send email with verification link
def verify_email(request):
    if request.method == "POST":
        if request.user.email_is_verified != True:
            current_site = get_current_site(request)
            user = request.user
            email = request.user.email
            subject = "Verify Email"
            message = render_to_string('users/verify_email_message.htm', {
                'request': request,
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            email = EmailMessage(
                subject, message, to=[email]
            )
            email.content_subtype = 'html'
            email.send()
            return redirect('core:verify-email-done')
        else:
            return redirect('core:signup')
    return render(request, 'users/verify_email.htm')

def verify_email_done(request):
    return render(request, 'users/verify_email_done.htm')

def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.email_is_verified = True
        user.save()
        messages.success(request, 'Your email has been verified.')
        return redirect('core:verify-email-complete')   
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'users/verify_email_confirm.htm')


def verify_email_complete(request):
    return render(request, 'users/verify_email_complete.htm')



#--------------------------------------------------------
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
    
    return JsonResponse({'message': 'Invalid request method'}, status=400)

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Username already exists'}, status=400)
        
        user = User.objects.create_user(username=username, password=password)
        
        if user is not None:
            return JsonResponse({'message': 'Registration successful'})
        else:
            return JsonResponse({'message': 'Registration failed'}, status=500)
    
    return JsonResponse({'message': 'Invalid request method'}, status=400)


@csrf_exempt
def user_update(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_username = request.POST.get('new_username')
        new_password = request.POST.get('new_password')
        
        user = authenticate(request, username=username)
        
        if user is not None:
            user.username = new_username
            user.set_password(new_password)
            user.save()
            
            return JsonResponse({'message': 'User update successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
    
    return JsonResponse({'message': 'Invalid request method'}, status=400)

# ------------------------------------------- model apis
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BranchSerializer


@api_view(['GET', 'POST'])
def branch(request):
    if request.method == 'POST':
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            # Process the validated data
            # Access the validated data using serializer.validated_data
            return Response(serializer.validated_data, status=201)
        else:
            return Response(serializer.errors, status=400)
    branch = m.Branch.objects.all()
    serializer = BranchSerializer(branch, many=True)
    serialized_data = serializer.data
    return Response(serialized_data)

def branch_is_new(request, key):
    if key