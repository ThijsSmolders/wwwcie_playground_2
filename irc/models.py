from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Memo(models.Model):
    guest = models.ForeignKey(User)
    memo = models.TextField()
# time = models.DateTimeField()
