from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.ProfileCreate.as_view(), name='signup'),
    path('profile/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('profile/<int:pk>/edit/', views.ProfileEdit.as_view(), name='profile_update'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/new/', views.AddPostView.as_view(), name='add_post')
]