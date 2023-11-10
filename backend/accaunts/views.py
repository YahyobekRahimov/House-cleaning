from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .tokens import account_activation_token
from accaunts.forms import UserRegisterForm, PasswordResetForm, SetPasswordForm

User = get_user_model()

def signup_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('accaunts/verify_email_message.htm', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return JsonResponse({'message': 'Activation email sent successfully'})
        else:
            return JsonResponse({'message': 'Invalid form data'}, status=400)

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return JsonResponse({'message': 'Account activated successfully'})
    else:
        return JsonResponse({'message': 'Invalid activation link'}, status=400)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)
    return JsonResponse({'message': 'Invalid request method'}, status=400)

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                user = User.objects.get(email=email)
                current_site = get_current_site(request)
                mail_subject = 'Reset your password'
                message = render_to_string('users/password_reset_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                email = EmailMessage(mail_subject, message, to=[email])
                email.send()
                return JsonResponse({'message': 'Password reset email sent successfully'})
            except User.DoesNotExist:
                return JsonResponse({'message': 'User does not exist'}, status=400)
        else:
            return JsonResponse({'message': 'Invalid form data'}, status=400)
    else:
        form = PasswordResetForm()
    context = {
        'form': form
    }
    return render(request, 'users/password_reset.html', context)

def password_reset_confirm(request, uidb64, token):
    if request.method == 'POST':
        uid = force_str(urlsafe_base64_decode(uidb64))
        try:
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Password reset successful'})
            else:
                return JsonResponse({'message': 'Invalid form data'}, status=400)
        else:
            return JsonResponse({'message': 'Invalid reset link'}, status=400)
    else:
        form = SetPasswordForm()
    context = {
        'form': form,
        'uidb64': uidb64,
        'token': token
    }
    return render(request, 'users/password_reset_confirm.html', context)
