from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth import login
from .forms import ProfileUpdateForm, UserRegistrationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:home')
       
        form = UserRegistrationForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} registered successfully')
            login(request, user)
            return redirect('blog:home')
        return render(request, 'user/register.html', {'form': form})


@login_required
def me(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('user:profile')
    else:
        user_form = UserRegistrationForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'user/me.html', context)
        
    
