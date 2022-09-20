# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path, include
from app import views
# from app import dash_nas

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    # path('nasional/', views.nasional, name='nasional'),
    # path('regional/', views.regional, name='regional'),
    # path('analytics/', views.analytics, name='analytics'),
    # path('profil/', views.profil, name='profil'),
    path('wallet/', views.wallet, name='wallet'),
    path('olahraga/', views.olahraga, name='olahraga'),
    path('activity/', views.activity, name='activity'),
    path('airquality/', views.airquality, name='airquality'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('hospital/', views.hospital, name='hospital'),
    path('government/', views.government, name='government'),
    # path('cluster/', views.cluster, name='cluster'),
    # path('verdict/', views.verdict, name='verdict'),
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    # django-dash
    # path('django_plotly_dash/', include('django_plotly_dash.urls')), 

]
