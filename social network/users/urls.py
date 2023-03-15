from django.contrib import admin
from django.urls import path
from users.views import loginn, signup, logout_view, user_listt, profile, user_detail, edit_profile

app_name = 'users'

urlpatterns = [
    path('login/', loginn, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('user_list/', user_listt, name='user_list'),
    path('profile/<str:username>/', profile, name='profile'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
