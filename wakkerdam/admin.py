
from django.contrib.admin import site
from wakkerdam.models import Game, Player

site.register(Player)
site.register(Game)


