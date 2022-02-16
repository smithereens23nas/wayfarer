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
    model = Post
    template_name = 'home.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'addPost.html'
    fields = '__all__'


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    fields = '__all__'

class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profile_detail.html'

class ProfileCreate(CreateView):
    form = UserCreationForm
    model = Profile
    fields = ['user_name', 'email', 'current_city', 'profile_picture']
    template_name = 'registration/profile_create.html'
    success_url = reverse_lazy('login')

class ProfileEdit(UpdateView):
    form_class = UserChangeForm
    model = Profile
    fields = ['user_name', 'email', 'current_city', 'profile_picture']
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user

class PostCreate(View):
    def post(self, request, pk):
        current_city = request.POST.get('current_city')
        title = request.POST.get('title')
        img = request.POST.get('img')
        body = request.POST.get('body')
        profile = Profile.objects.get(pk=pk)
        Post.objects.create(current_city=current_city, title=title, img=img, body=body, profile=profile)
        return redirect('profile_detail')


