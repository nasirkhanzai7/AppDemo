from django.urls import path
from .views import Users, GetUserById, Meetings,GetMeetings, Subscriptions

urlpatterns = [
    path('userslist/', Users, name='userList'),
    path('getuser/<int:id>/', GetUserById, name='getUsers'),
    path('meetingslist/', Meetings, name='userList'),
    path('getusermeeting/<int:id>/', GetMeetings, name='userList'),
    path('subscriptionslist/', Subscriptions, name='userList'),

]
