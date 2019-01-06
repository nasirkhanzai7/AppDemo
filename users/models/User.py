from django.db import models
from .UserSubscription import UserSubscription


class User(models.Model):
    Name = models.CharField(max_length=120)
    Surname = models.CharField(max_length=120)
    Company = models.CharField(max_length=120, null=True, blank=True)
    Job_Title = models.CharField(max_length=120, null=True, blank=True)
    Auth_Token = models.CharField(max_length=120, null=True, blank=True)
    Device_ID = models.CharField(max_length=120, null=True, blank=True)
    State = models.CharField(max_length=120, null=True, blank=True)
    Culture_Info = models.CharField(max_length=120, null=True, blank=True)
    Subscription = models.ForeignKey(UserSubscription, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name + ' ' + self.Subscription.Name
