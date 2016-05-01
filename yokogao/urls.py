# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'repos$', views.repo_list, name='repo_list'),
    url(r'repo/(?P<repo_name>[\w-]+)', views.repo_detail, name='repo_detail'),
    url(r'followers$', views.follower_list, name='follower_list'),
    url(r'following$', views.following_list, name='following_list')
]
