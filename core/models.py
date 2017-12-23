from django.db import models

# Create your models here.


class Note(models.Model):
    label = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.label

