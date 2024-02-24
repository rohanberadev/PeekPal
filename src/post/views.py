from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from .forms import CreatePostForm, PredictOnPostForm
from django.contrib.auth.models import User
from .models import Post

@login_required(login_url='/login/')
@require_POST
def create_post (request):
    user = User.objects.filter(username=request.user).first()
    
    if user is None:
        return redirect('/forbidden/')
    
    form = CreatePostForm(request.POST)
    if form.is_valid():
        hint_or_question = form.cleaned_data['hint_or_question']
        answer = form.cleaned_data['answer']
        option1 = form.cleaned_data['option1']
        option2 = form.cleaned_data['option2']
        option3 = form.cleaned_data['option3']
        option4 = form.cleaned_data['option4']

        if answer not in [option1, option2, option3, option4]:
            return redirect('/home/')

        new_post = Post.objects.create(user=user, hint_or_question=hint_or_question, answer=answer, option1=option1, option2=option2, option3=option3, option4=option4)
        new_post.save()
        return redirect('/home/')
    
    

@login_required(login_url='/login/')
@require_POST
def predict_on_post (request):
    pass
    
