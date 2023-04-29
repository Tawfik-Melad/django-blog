from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm , UserUpdateForm,ProfileUpdateForm
from django.views.generic import (
    ListView,
)
from blog.models import Post
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated ')
            return redirect('profile' , username=request.user.username)
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)        
    context={'u_form':u_form,'p_form':p_form}
    return render(request,'users/profile_update.html',context)


class ProfileListView(ListView):
    template_name='users/profile.html'
    context_object_name='posts'
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs['username'])
        return Post.objects.filter(author=user)
