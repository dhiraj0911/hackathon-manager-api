from django.urls import path
from .views import (
    HackathonList, HackathonDetails, HackathonParticipation, 
    HackathonSubmissions, UserHackathonList)

urlpatterns = [
    path('hackathons/', HackathonList.as_view()),
    path('hackathons/<int:pk>/', HackathonDetails.as_view()),
    path('hackathons/participate/<int:pk>/', HackathonParticipation.as_view()),
    path('hackathons/user/submissions/<int:pk>/', HackathonSubmissions.as_view()),
    path('hackathons/user/participating/', UserHackathonList.as_view()),
]