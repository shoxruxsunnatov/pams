from datetime import timedelta

from django.db import models
from django.utils import timezone

from main.utils import get_token


class AccessKey(models.Model):
    token = models.CharField(max_length=200, null=True, blank=True)
    times_used = models.IntegerField(default=0)
    date_expiration = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date_created}"

    def save(self, *args, **kwargs):

        if not self.token:
            self.token = get_token()
        
        if not self.date_expiration:
            self.date_expiration = timezone.now() + timedelta(days=7)

        super().save(*args, **kwargs)

