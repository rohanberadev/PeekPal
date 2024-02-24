from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import CreateUserForm, LoginUserForm

def register_user (request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            # check if both passwords are same.
            if password1 != password2:
                messages.error(request, "Both password should match.") 
                return redirect('/register/')

            # check if username already exist.
            if User.objects.filter(username=username).first():
                messages.error(request, "Username is already taken.")
                return redirect('/register/')
            
            # check if email has been already used to create an account.
            if User.objects.filter(email=email).first():
                messages.error(request, "This email has been already used to create an account.")
                return redirect('/login/')

            user = User.objects.create_user(username=username, password=password2, email=email)

            if user is not None:
                user.save()
                messages.success(request, "Account has been successfully created.")
                return redirect('/login/')
            
            messages.error(request, "Someting went wrong.") 
            return redirect('/register/')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('/register/')

    form = CreateUserForm()
    return render(request, "pages/register.html", {"form": form})


def login_user (request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']

            # autehnticating user.
            user = authenticate_user(request, username_or_email, password)

            # authentication is successfull.
            if user is not None:
                return redirect('/home/')
            
            messages.error(request, "Username / email or password is incorrect.")
            return redirect('/login/')

    form = LoginUserForm()
    return render(request, "pages/login.html", {"form": form})


def authenticate_user (request, username_or_email: str, password: str) -> User | None:
    # checking if email exist.
    user = User.objects.filter(email=username_or_email).first()

    # if email doesn't exist then check if username exist. 
    if not user:
        # checking if username exist.
        user = User.objects.filter(username=username_or_email).first()
    
    if user and user.check_password(password) and user.is_active:
        # creating session.
        login(request, user)
        return user

    return None