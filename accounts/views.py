from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .forms import SignupForm
from django.contrib.auth import authenticate , login
from .models import Profile
from .forms import UserForm,ProfileForm
from django.contrib.auth.models import User
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
    if request.method=='GET':
        
        profile=get_object_or_404(Profile,user=request.user)
        return render(request,'accounts/profile.html',{'profile':profile})

def edit_profile(request):
    profile=get_object_or_404(Profile,user=request.user)
    user=get_object_or_404(User,username=request.user)
    # profilee=Profile.objects.get(id=id)
    if request.method=='GET':
        profileForm=ProfileForm(instance=profile)
        userForm=UserForm(instance=user)
        return render(request,'accounts/edit_profile.html',{'profileForm':profileForm,'userForm':userForm})
    else:
        profileForm=ProfileForm(request.POST,request.FILES,instance=profile)
        userForm=UserForm(request.POST,instance=user)
        if profileForm.is_valid() and userForm.is_valid():
            profileForm.save()
            userForm.save()
        # return render(request,'accounts/edit_profile.html',{'form':profileForm})
        return redirect(reverse('accounts:profile'),{'profile':profile})
        