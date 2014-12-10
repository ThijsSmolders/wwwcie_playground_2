
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from wakkerdam.views import all_games, make_game, make_game_submit, show_game, game_not_found, join_game, info


urlpatterns = patterns('',
	url(r'^$', lambda request: HttpResponseRedirect(reverse('wakkerdam_games_all'))),
	url(r'^games/$', all_games, name = 'wakkerdam_games_all'),
	url(r'^make_game/$', make_game, name = 'wakkerdam_make_game'),
	url(r'^make_game/submit/$', make_game_submit, name = 'wakkerdam_make_game_submit'),
	url(r'^game/$', show_game, name = 'wakkerdam_game'),
	url(r'game_not_found/$', game_not_found, name = 'wakkerdam_game_not_found'),
	url(r'join_game/$', join_game, name = 'wakkerdam_join_game'),
	url(r'info/$', info, name = 'wakkerdam_info'),
)


