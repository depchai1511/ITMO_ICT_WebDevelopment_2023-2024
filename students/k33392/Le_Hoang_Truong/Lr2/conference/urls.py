from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    
    path('login/', views.login, name='login'),
    path('create/', views.create_conference, name='create_conference'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.list_conference),
    path('<int:id>/', views.conference,name = 'conference'),
    path('register/<int:conference_id>/', views.register_conference),
    path('cancel_registration/<int:conference_id>/', views.cancel_registration),
    path('participants/<int:id>/', views.list_participant,name ="participants"),
    path('profile/',views.profile,name='profile'),
    path("profile/<pk>/update", views.UserUpdateView.as_view(), name="update_user"),
]
