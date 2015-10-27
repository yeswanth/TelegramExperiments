from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url('^/(?P<token>.+)/$','telegram_bot.views.webhook','webhook'),
)
