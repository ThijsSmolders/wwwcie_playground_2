from django.db import models
from django.contrib.auth.models import User

class Bericht(models.Model):
    user = models.ForeignKey(User)
    msg = models.TextField()
#    when =
