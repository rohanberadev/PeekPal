from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from .models import Friend, FriendRequest
from notification.models import FreindRequestNotification
from .forms import AddFriendForm, FriendRequestForm
from django.contrib import messages

@login_required(login_url='/login')
def get_user_friend (user: User):
    friends = Friend.objects.filter(user=user)
    return friends


@login_required(login_url='/login')
@require_POST
def send_friend_request (request):
    # get user who requested
    requested_by = User.objects.filter(username=request.user).first()
    
    # check if user exist
    if requested_by is None:
        return redirect('/forbidden/')
    
    form = AddFriendForm(request.POST)
    if form.is_valid():
        # get user_id from form
        user_id = form.cleaned_data['user_id']

        # check if user who send request is not same as recieve user
        if user_id == requested_by.id:
            return redirect('/forbidden/')

        # get user to send the request
        requested_to = User.objects.filter(id=user_id)
        
        # check if user to send request exist
        if requested_to is None:
            return redirect("/forbiddden/")
        
        # check if they are already a friend
        if check_friend_exist(requested_by, requested_to):
            return redirect('/forbidden/')
        
        # check if user already send a request
        if check_friend_request_exist(requested_by, requested_to):
            return redirect('/forbidden/')
        
        # create friend request
        friend_request = FriendRequest.objects.create(requested_by=requested_by, requested_to=requested_to)

        # create friend request notification
        FreindRequestNotification.objects.create(send_from=requested_by, send_to=requested_to, friend_request=friend_request)

        # send success message and redirect to home
        messages.success(request, f"Freind request has been successfully sent to {requested_to.username}")
        return redirect('/home/')

    messages.error(request, "Something went wrong.")
    return redirect('/home/')


@login_required(login_url='/login/')
@require_POST
def accept_friend_request (request):
    pass


def check_friend_exist (user1, user2) -> bool:
    return Friend.objects.exists(user=user1, friend=user2) or Friend.objects.exists(user=user2, friend=user1)


def check_friend_request_exist (requested_by, requested_to) -> bool:
    return FriendRequest.objects.exists(requested_by=requested_by, requested_to=requested_to)
