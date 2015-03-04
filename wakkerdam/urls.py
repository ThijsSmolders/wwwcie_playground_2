
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from start_views import all_games, make_game, make_game_submit, show_game, game_not_found, join_game, info, \
	start_game, leave_game, start_phase_two
from game_views import play_night, play_day, wait_for_votes


urlpatterns = patterns('',
	url(r'^$', lambda request: HttpResponseRedirect(reverse('wakkerdam_games_all'))),
	url(r'^games/$', all_games, name = 'wakkerdam_games_all'),
	url(r'^make_game/$', make_game, name = 'wakkerdam_make_game'),
	url(r'^make_game/submit/$', make_game_submit, name = 'wakkerdam_make_game_submit'),
	url(r'^game/$', show_game, name = 'wakkerdam_game'),
	url(r'game_not_found/$', game_not_found, name = 'wakkerdam_game_not_found'),
	url(r'join_game/$', join_game, name = 'wakkerdam_join_game'),
	url(r'info/$', info, name = 'wakkerdam_info'),
	url(r'start_game/$', start_game, name = 'wakkerdam_start_game'),
	url(r'leave_game/$', leave_game, name = 'wakkerdam_leave_game'),
	url(r'start_phase_two/$', start_phase_two, name = 'wakkerdam_start_phase_two'),
	url(r'night/$', play_night, name = 'wakkerdam_night'),
	url(r'day/$', play_day, name = 'wakkerdam_day'),
	url(r'wait/', wait_for_votes, name='wakkerdam_waiting_room'),
)


