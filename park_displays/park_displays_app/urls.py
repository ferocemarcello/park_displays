from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
path('emergency', views.emergency, name='index'),
path('login', views.login, name='login'),
path('parkdetails', views.parkdetails, name='parkdetails'),
path('similarusers', views.similarusers, name='similarusers'),
path('sportrec', views.sportrec, name='sportrec'),
path('weather', views.weather, name='weather'),
path('outdoorgym', views.outdoorgym, name='outdoorgym'),
path('runwalk', views.runwalk, name='runwalk'),
path('freeweight', views.freeweight, name='freeweight'),
path('groupfitness', views.groupfitness, name='groupfitness'),
path('findgroups', views.findgroups, name='findgroups'),
path('login', views.login, name='login'),
path('startpage', views.startpage, name='startpage'),
path('freeweight', views.freeweight, name='freeweight'),
path('weather', views.weather, name='weather'),
path('emergency', views.emergency, name='emergency'),

path('parkdetails', views.parkdetails, name='parkdetails'),
path('run_walk_recommendation', views.run_walk_recommendation, name='run_walk_recommendation'),
path('gym_recommendation', views.gym_recommendation, name='gym_recommendation'),
path('freeweight_recommendation', views.freeweight_recommendation, name='freeweight_recommendation'),
path('get_grouprecommendations', views.get_grouprecommendations, name='get_grouprecommendations'),
path('runwalkrecresult', views.runwalkrecresult, name='runwalkrecresult'),
path('freeweightrecresult', views.freeweightrecresult, name='freeweightrecresult'),
path('gymrecresult', views.gymrecresult, name='gymrecresult'),
path('grouprecresult', views.grouprecresult, name='grouprecresult'),
path('path_detail',views.path_detail,name='path_detail')
]
