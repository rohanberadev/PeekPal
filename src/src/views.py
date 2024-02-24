from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from post.models import Post, PostPrediction
from django.contrib import messages

from .forms import SearchUserForm

def main_page (request):
    return render(request, "pages/main.html")

@login_required(login_url='/login/')
def home_page (request):
    return render(request, "pages/home.html", {"data": ["1", "2", "3", "4"], "display": "true"})

@login_required(login_url='/login/')
def notifications_page (request):
    return render(request, "pages/notifications.html")

@login_required(login_url='/login/')
def peeks_page (request):
    return render(request, "pages/peeks.html", {"data": ["1", "2", "3", "4"]})

@login_required(login_url='/login/')
def vault_page (request):
    return render(request, "pages/vault.html")

@login_required(login_url='/login/')
def friends_page (request):
    return render(request, "pages/friends.html")

@login_required(login_url='/login/')
def profile_page (request):
    context = {
        "activeLink": "posts" 
    }
    return render(request, "pages/profile.html", context=context)

@login_required(login_url='/login/')
@require_POST
def search_user (request):
    form = SearchUserForm(request.POST)
    if form.is_valid():
        username_to_search = form.cleaned_data['username']
        return redirect(f'/user/{username_to_search}')

def user_profile (request,username=None):
    found_user = User.objects.filter(username=username).values().first()

    context = {
        "username": username
    }

    if found_user:
        return render(request, "test.html", context=context)
    else:
        return redirect('/not-found')
    
def not_found (request):
    return render(request,"pages/notfound.html")