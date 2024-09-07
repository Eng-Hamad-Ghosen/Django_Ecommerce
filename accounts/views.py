from django.shortcuts import render,get_object_or_404
from .forms import SignupForm
from django.contrib.auth import authenticate , login
from .models import Profile
# Create your views here.

def signup(request):
    if request.method=='GET':
        form = SignupForm()
        
    else:
        form=SignupForm(request.POST)
        if form.is_valid():
            if request.POST['password1']==request.POST['password2']:
                form.save(commit=False)
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                print(form.fields)
                user = authenticate(request,username=username,password=password)
                login(request,user)
    return render(request,'registration/signup.html',{'form':form})

def profile(request):
    # profile=Profile.objects.get(user=request.user)
    profile=get_object_or_404(Profile,user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})