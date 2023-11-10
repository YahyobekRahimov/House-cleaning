from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import random
from core import models as m



def generate_random_number():
    return random.randint(100000, 999999)

def send_email_code(email, random_number):
    subject = 'Authorization Code'
    message = f'Your authorization code is: {random_number}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def home(request):
    # random_number = generate_random_number()
    # send_email_code('niddihur@gmail.com', random_number)
    return HttpResponse('home')
