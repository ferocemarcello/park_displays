from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
path('emergency', views.emergency, name='index'),
path('login', views.login, name='login'),
path('parkdetails', views.parkdetails, name='parkdetails'),
path('similarusers', views.similarusers, name='similarusers'),
path('social', views.social, name='social'),
path('sportrec', views.sportrec, name='sportrec'),
path('weather', views.weather, name='weather'),
path('outdoorgym', views.outdoorgym, name='outdoorgym'),
path('runwalk', views.runwalk, name='runwalk'),
path('freeweight', views.freeweight, name='freeweight'),
path('groupfitness', views.groupfitness, name='groupfitness'),
path('findgroups', views.findgroups, name='findgroups'),
path('grouprecommendations', views.grouprecommendations, name='grouprecommendations'),
path('login', views.login, name='login'),
path('startpage', views.startpage, name='startpage'),
]
