from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('signup/', views.ProfileCreate.as_view(), name='signup'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('profile/new/', views.ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:pk>/edit/', views.ProfileEdit.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile_delete'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/new/', views.AddPostView.as_view(), name='add_post')
]