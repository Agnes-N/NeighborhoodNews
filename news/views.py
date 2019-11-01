from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .email import send_welcome_email
from .models import NewsLetterRecipients,Profile,Neighborhood
from .forms import NewProfileForm,NewNeighborhoodForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    all_hoods = Neighborhood.objects.all()
    return render(request, 'welcome.html', {"all_hoods": all_hoods})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('myprofile')

    else:
        form = NewProfileForm()
    return render(request, 'edit_profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def my_profile(request):

    current_user = request.user
    # my_projects = Project.objects.filter(user = current_user)
    my_profile = Profile.objects.filter(user = current_user).first()
    return render(request, 'profile.html', { "my_profile":my_profile})

@login_required(login_url='/accounts/login/')
def add_neighborhood(request):

    current_user = request.user
    if request.method == 'POST':
        form = NewNeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.save()
        return redirect('welcome')

    else:
        form = NewNeighborhoodForm()
    return render(request, 'add_hood.html', {"form": form})


def neigborhood(request,id):
        hoods = Neighborhood.filter_neigborhood_by_id(id)
        return render(request,'neigborhood.html', {"hoods":hoods})











def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'Your account has been successfully created'}
    return JsonResponse(data)