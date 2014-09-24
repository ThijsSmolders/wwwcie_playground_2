from django.conf.urls import patterns, include, url
from django.contrib import admin
from msn.views import msn_chat
from irc.views import irc

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wwwcie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^msn/', msn_chat),
    url(r'^irc/', irc),
)
