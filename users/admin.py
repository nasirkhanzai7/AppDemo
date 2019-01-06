from django.contrib import admin
from .models import UserSubscription, User, Meeting
# Register your models here.
admin.site.register(UserSubscription)
admin.site.register(User)
admin.site.register(Meeting)
