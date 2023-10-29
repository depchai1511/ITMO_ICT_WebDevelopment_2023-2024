from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Conference, Comment, Registration, PresentationResult,User
from .forms import RegistrationForm
from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import UserUpdateForm
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
# Create your views here.


def index(request):
    return render(request, 'pages/home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            auth_login(request,user)  
            return HttpResponseRedirect('/')
        else:
            return render(request, 'pages/login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'pages/login.html')

def user_logout(request):
    auth_logout(request)
    return redirect('/') 

def profile(request) :
    user = request.user
    conferences_attended = user.presentation_results.all().values_list('conference', flat=True)
    conferences = Conference.objects.filter(pk__in=conferences_attended)

    return render(request,'pages/profile.html',{'user':user,'conferences':conferences})
def signup(request):

    form = RegistrationForm()

    if request.method == 'POST' :
        form = RegistrationForm(request.POST)
        if form.is_valid() :
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            auth_login(request,user) 
            return HttpResponseRedirect('/')
    return render(request, "pages/signup.html",{'form' : form})


def list_conference(request):
    if request.user.is_authenticated:
        user = request.user
        conferences = Conference.objects.all()
        registrations = Registration.objects.filter(
            conference__in=conferences, user=user)
        registered_conferences = set(
            registrations.values_list('conference_id', flat=True))
    else:
        conferences = Conference.objects.all()
        registered_conferences = set()

    data = {
        'Conferences': conferences,
        'RegisteredConferences': registered_conferences,
    }
    return render(request, 'pages/conferences.html', data)

def list_participant(request, id):
    try:
        conference = Conference.objects.get(id=id)
        participants = Registration.objects.filter(conference=conference)
    except Conference.DoesNotExist:
        raise Http404("Conference does not exist")
    except Registration.DoesNotExist:
        participants = []

    data = {
        'Participants': participants,
    }
    return render(request, 'pages/participants.html', data)
def conference(request, id):
    conference = Conference.objects.get(id=id)
    user = PresentationResult.objects.get(conference = conference).user
    result = conference.result
    recommended = conference.recommended
    comments = Comment.objects.filter(conference_id=id)

    if request.method == 'POST':
        user_id = request.user.id
        comment_text = request.POST.get('comment')
        rating = request.POST.get('rating')
        print(comment_text)
        if comment_text:
            comment = Comment(content=comment_text,
                              conference=conference, user_id=user_id,rating = rating)
            comment.save()

            comments = Comment.objects.filter(conference_id=id)

    return render(request, 'pages/conference.html', {'conference': conference, 'comments': comments,'user' : user,'result' :result,'recommended' : recommended})


def register_conference(request, conference_id):
    if request.user.is_authenticated:
        conference = Conference.objects.get(id=conference_id)
        Registration.objects.create(conference=conference, user=request.user)

    user = request.user
    conferences = Conference.objects.all()
    registrations = Registration.objects.filter(
        conference__in=conferences, user=user)
    registered_conferences = set(
        registrations.values_list('conference_id', flat=True))
    data = {
        'Conferences': conferences,
        'RegisteredConferences': registered_conferences,
    }
    return render(request, 'pages/conferences.html', data)


def cancel_registration(request, conference_id):
    if request.user.is_authenticated:
        conference = Conference.objects.get(id=conference_id)
        Registration.objects.filter(
            conference=conference, user=request.user).delete()

    user = request.user
    conferences = Conference.objects.all()
    registrations = Registration.objects.filter(
        conference__in=conferences, user=user)
    registered_conferences = set(
        registrations.values_list('conference_id', flat=True))
    data = {
        'Conferences': conferences,
        'RegisteredConferences': registered_conferences,
    }
    return render(request, 'pages/conferences.html', data)

def create_conference(request):
    if request.method == 'POST':
        name = request.POST['name']
        decription = request.POST['decription']
        location = request.POST['location']
        user = request.user
        conference = Conference(name =name,decription = decription,location = location)
        conference.save()
        PresentationResult(user=user,conference=conference).save()
        return HttpResponseRedirect('/')

    return render(request, 'pages/create_conference.html')

class UserUpdateView(UpdateView):
    model = User
    template_name = "pages/update_user.html"
    form_class = UserUpdateForm
    success_url = "/profile"