# -*- coding: utf-8 -*-
"""
Do not go gentle into that good night

Created on Tue Oct  9 23:53:25 2018

@author: Kenzo Yan
"""

from django.conf.urls import url
from . import views
from django.urls import path,include
urlpatterns = [
    url('^$', views.post_list,name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]