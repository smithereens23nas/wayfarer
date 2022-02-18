from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login
from .models import Profile, Post, City


# Create your views here.

class Home(ListView):
    model = City
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cities"] = City.objects.all()
        return context
class AddPostView(CreateView):
    model = Post
    template_name = 'addPost.html'
    fields = '__all__'
    

class PostList(TemplateView):
    template_name = 'post_list.html'
    def get_context_data(self, **kwargs): #what are kwargs??
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['posts'] = Post.objects.filter(name__icontains=name)
            context['header'] = f"Searching For {name}"
        else:
            context['posts'] = Post.objects.all()
            context['header'] = "All Posts"
        return context

class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    def get_context_data(self, **kwargs): #what are kwargs??
        context = super().get_context_data(**kwargs)
        # author = kwargs['object']
        name = self.request.GET.get('profile')
        print(self.kwargs)        
        context['posts'] = Post.objects.filter(author=self.kwargs['pk'])
        return context

class ProfileCreate(CreateView):
    form = UserCreationForm
    model = Profile
    fields = ['user', 'name', 'email', 'city', 'profile_picture']
    template_name = 'profile_create.html'
    success_url = reverse_lazy('login')

class ProfileEdit(UpdateView):
    model = Profile
    fields = ['user', 'name', 'email', 'city', 'profile_picture']
    template_name = 'profile_update.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user


class ProfileDelete(DeleteView):
    model = Profile
    template_name = 'profile_delete.html'
    success_url = '/posts/'



class PostCreate(View):
    def post(self, request, pk):
        current_city = request.POST.get('city_id')
        title = request.POST.get('title')
        img = request.POST.get('img')
        body = request.POST.get('body')
        profile = Profile.objects.get(pk=pk)
        Post.objects.create(city_id=current_city, title=title, img=img, body=body, profile=profile)
        return redirect('profile_detail')
    

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = '/posts/'


class PostEdit(UpdateView):
    model = Post
    fields = ['title', 'city', 'img', 'body', 'author' ]
    template_name = 'post_update.html'
    success_url = '/posts/'

# class LoginView(View):
#     redirect('login.html')


