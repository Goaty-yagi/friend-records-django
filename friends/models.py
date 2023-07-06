from django.db import models

from users.models import User

from django.utils import timezone



class Friend(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name='character', default=None, on_delete=models.CASCADE)
    sum = models.IntegerField(default=0)
    birthday = models.DateField(default=None, null=True, blank=True)
    thumbnail = models.ImageField(blank=True, null=True, default='default.png')
    avatar = models.CharField(max_length=50)
    last_log = models.DateTimeField(default=timezone.now, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)


    class Meta:
        ordering = ['-last_log',]

    def __str__(self):
        return self.name