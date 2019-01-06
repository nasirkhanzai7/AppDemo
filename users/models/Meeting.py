from django.db import models
from .User import User


class Meeting(models.Model):
    Location = models.CharField(max_length=120)
    Time = models.DateTimeField(max_length=120)
    UserA = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserA')
    UserB = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserB')

    def __str__(self):
        return self.Location + ' ' + str(self.Time.date()) + ' ' + str(self.Time.time())
