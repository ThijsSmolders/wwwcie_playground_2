
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
from msn.views import msn_chat
from irc.views import irc
from wakkerdam.views_account import login, login_submit, logout, logout_submit, register, register_submit


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'wwwcie.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^msn/', msn_chat),
	url(r'^irc/', irc),
	url(r'^$', lambda request: HttpResponseRedirect('/wakkerdam/')),
	url(r'^wakkerdam/', include('wakkerdam.urls')),
	url(r'account/login/$', login, name = 'wakkerdam_login'),
	url(r'account/login/submit$', login_submit, name = 'wakkerdam_login_submit'),
	url(r'account/logout/$', logout, name = 'wakkerdam_logout'),
	url(r'account/logout/submit/$', logout_submit, name = 'wakkerdam_logout_submit'),
	url(r'account/register/$', register, name = 'wakkerdam_register'),
	url(r'account/register/submit/$', register_submit, name = 'wakkerdam_register_submit'),
)


