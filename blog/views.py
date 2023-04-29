from django.shortcuts import render ,get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['date']
    

class PostDetailView(DetailView):
    model=Post


class PostCreatView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['isCreat'] = 1
        return context
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['isCreat'] = 0
        return context

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if post.author == self.request.user:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if post.author == self.request.user:
            return True
        return False

def Like_post(request,pk):
    post=get_object_or_404(Post,id = pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(request.META['HTTP_REFERER'])

def about_view(request):
    return render(request,'blog/about.html')
