from django.conf.urls import url
from ask_me.views import *

# app_name = 'ask_me'
urlpatterns = [
    url(r'^$', main),
    url(r'^questions/$', questions, name='questions'),
    url(r'^login/$', login, name='login'),
    url(r'^registration/$', registration, name='registration'),
    url(r'^ask/$', new_ask, name='new_ask'),
    url(r'^settings/$', settings, name='settings'),
    url(r'^tag/bender/$', tag, name='tag'),
    url(r'^question/1232343', question, name='question')
]

