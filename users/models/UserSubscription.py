from django.db import models


class UserSubscription(models.Model):
    Name = models.CharField(max_length=120)
    Description = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.Name
