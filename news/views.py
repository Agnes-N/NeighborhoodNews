from django.shortcuts import render
from .email import send_welcome_email
from .models import NewsLetterRecipients
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    message = "Welcome"
    return render(request, 'welcome.html', {"message": message})

def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'Your account has been successfully created'}
    return JsonResponse(data)