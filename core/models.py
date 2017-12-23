from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    label = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.label


