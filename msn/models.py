from django.db import models
from django.contrib.auth.models import User

class Bericht():
    user = models.ForeignKey(User)
    msg = models.TextField()
#    when =
