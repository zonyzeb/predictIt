"""guesskaro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('match', views.match,name="match"),
    path('team', views.team,name="team"),
    path('result', views.result,name="result"),
    path('leader_board',views.leader_board,name="leader_board"),
    path('matches/<str:date>/', views.match_date),
    path('matches/upcoming', views.match_upcoming),
    path('matches/prediction', views.match_predict),
    # path('hello/', views.HelloView.as_view(), name='hello'),
    path('login', obtain_auth_token, name='api_token_auth'),
]
