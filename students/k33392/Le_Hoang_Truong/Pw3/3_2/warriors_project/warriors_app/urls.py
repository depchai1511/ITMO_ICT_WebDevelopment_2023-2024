from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', WarriorAPIView.as_view(), name='warrior-list'),
   path('profession/create/', ProfessionCreateView.as_view()),
   path('skills/', SkillListView.as_view(), name='skill-list'),
    path('warriors/<int:id>/', WarriorDetailAPIView.as_view(), name='warrior-detail'),
]