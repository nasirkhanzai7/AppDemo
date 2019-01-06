from .utils.JSONResponse import  jsonResponse
from .models.User import User
from .models.Meeting import Meeting
from .models.UserSubscription import UserSubscription
from django.db.models import Q


def Users(request):
    users = User.objects.all()
    return jsonResponse(users)


def GetUserById(request, id):
    users = User.objects.filter(pk=id)
    return jsonResponse(users)


def Subscriptions(request):
    subscriptions = UserSubscription.objects.all()
    return jsonResponse(subscriptions)


def GetMeetings(request, id):
    subscriptions = Meeting.objects.filter(Q(UserA=id) | Q(UserB=id))
    return jsonResponse(subscriptions)


def Meetings(request):
    meeting = Meeting.objects.all()
    return jsonResponse(meeting)
