import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json

# Create your views here.
from .xmlmanager import XmlManager
from .recommendation import RunWalkRecommender
from .data_manager import ParkManager,DataProcesser,AthleteManager
from .forms import CheckMultiCheckBox
from .forms import CheckBox
from .forms import Dropdown

path_types=XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_filters.xml").getPathTypes()
gymtool_types = XmlManager(
        os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_filters.xml").getToolTypes()

def index(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {

        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_INDEX",
    }
    return HttpResponse(template.render(context, request))
def emergency(request):
    template = loader.get_template('park_displays_app/emergency.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_EMERGENCY",
    }
    return HttpResponse(template.render(context, request))
def weather(request):
    template = loader.get_template('park_displays_app/weather.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_WEATHER",
    }
    return HttpResponse(template.render(context, request))
def runwalkrecresult(request):

    '''inputf = FormClass(None,request.POST, request.FILES)
    inputf2 = FormClass(request.POST)
    if request.method == 'POST' and inputf.is_valid() and inputf2.is_valid():
        if len(request.FILES.getlist('file_field')) == 2:
            coordinatesfile = request.FILES.getlist('file_field')[0]'''
    gender="male"
    age=31
    weight=75
    height=186
    kcal=700
    avgweekkm=40
    activity="running"
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "athletes.xml")
    shoetype=AthleteManager(0,xmlmng).getShoeType()
    pathrecommendations=RunWalkRecommender(gender=gender,age=age,weight=weight,height=height,kcal=kcal,avgweekkm=avgweekkm,activity=activity).recommendPaths()
    template = loader.get_template('park_displays_app/run_walk_recommendation_result.html')
    context = {
        'pathrecommendations':pathrecommendations,
    }
    return HttpResponse(template.render(context, request))
def sportrec(request):
    template = loader.get_template('park_displays_app/recommendation.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_SPORT_REC",
    }
    return HttpResponse(template.render(context, request))

def social(request):
    template = loader.get_template('park_displays_app/startpage.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_SOCIAL",
    }
    return HttpResponse(template.render(context, request))
def login(request):
    template = loader.get_template('park_displays_app/login.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_LOGIN",
    }
    return HttpResponse(template.render(context, request))
def similarusers(request):
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    datamng = ParkManager("englischer_garten", xmlmng, pathtypes=path_types, gymtooltypes=gymtool_types)
    runners=datamng.getRunners()
    walkers=datamng.getWalkers()
    gymathletes=datamng.getGymAthletes()
    freeweightathletes=datamng.getFreeweightAthletes()
    stretchers = datamng.getStretchers()
    template = loader.get_template('park_displays_app/similarusers.html')
    context = {
        'runners':json.dumps(runners),
        'walkers':json.dumps(walkers),
        'gymathletes':json.dumps(gymathletes),
        'freeweightathletes':json.dumps(freeweightathletes),
        'stretchers':json.dumps(stretchers),
    }
    return HttpResponse(template.render(context, request))
def outdoorgym(request):
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    datamng = ParkManager("englischer_garten", xmlmng,pathtypes=path_types, gymtooltypes=gymtool_types)
    choices=[(x[0],x[0]) for x in datamng.getGymTools()]
    gymselectionmulticheck = CheckMultiCheckBox(choices=choices,label="Select Gym tools to show")
    template = loader.get_template('park_displays_app/outdoorgym.html')
    gymtools=datamng.getGymTools()
    gymtoolscoordinates=[]
    for gymtool in gymtools:
        gymtoolscoordinates.append(gymtool[1])
    gymtoolsbytype = datamng.getGymToolsByType()
    gymtoolsbytypedict = DataProcesser.listIntoDict(gymtoolsbytype)
    context = {
        'gymtoolscoordinates':json.dumps(gymtoolscoordinates),
        'gymtoolsbytype':json.dumps(gymtoolsbytypedict),
        'checkboxes': gymselectionmulticheck,
        'gymtooltypes': gymtool_types,
    }
    return HttpResponse(template.render(context, request))
def parkdetails(request):
    template = loader.get_template('park_displays_app/parkdetails.html')
    xmlmng=XmlManager(os.path.dirname(os.path.realpath(__file__))+os.sep+"xmldata"+os.sep+"park_data.xml")
    datamng = ParkManager("englischer_garten", xmlmng, pathtypes=path_types, gymtooltypes=gymtool_types)
    waterselection=CheckMultiCheckBox(choices=[('Water Fountains','Water Fountains')],label="Show water fountains")
    terrainchoices = [(x, x) for x in XmlManager(
        os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_filters.xml").getPathTypes()]
    pathselection = CheckMultiCheckBox(choices=terrainchoices,label="Filter path by terrain")
    pathselection.fields['selection'].widget.attrs['id']="terraintypeselection"
    fountainlist=datamng.getFountains()

    pathsformtatted=datamng.getPathsWaypoints()
    pathsbytype =datamng.getPathsByType()
    pathlenghts=datamng.getPathsLengths()
    pathslopes=datamng.getPathsSlopes()
    pathheightdiff=datamng.getPathsHeightdiffs()

    pathtypesdict=DataProcesser.listIntoDict(pathsbytype)
    pathheightdiffdict=DataProcesser.listIntoDict(pathheightdiff)
    pathslopesdict=DataProcesser.listIntoDict(pathslopes)
    pathlenghtsdict=DataProcesser.listIntoDict(pathlenghts)

    context = {
        'fountains': json.dumps(fountainlist),#water fountains
        'paths':json.dumps(pathsformtatted),#list of paths
        'pathtypes':json.dumps(pathtypesdict),#types of paths
        'watercheckbox':waterselection,#water fountain selection
        'pathcheckboxes':pathselection,#checkboxes with paths
        'pathheightdiffs':pathheightdiffdict,#dict of height differences of paths
        'pathslopes':pathslopesdict,#dict of slopes of paths
        'pathlenghts':pathlenghtsdict,#dict of lenghts of paths
    }
    return HttpResponse(template.render(context, request))

def runwalk(request):
    xml = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml")

    template = loader.get_template('park_displays_app/run_walk.html')
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    datamng = ParkManager("englischer_garten", xmlmng, pathtypes=path_types, gymtooltypes=gymtool_types)
    waterselection = CheckMultiCheckBox(choices=[('Water Fountains', 'Water Fountains')], label="Show water fountains")
    terrainchoices = [(x, x) for x in XmlManager(
        os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_filters.xml").getPathTypes()]
    pathselection = CheckMultiCheckBox(choices=terrainchoices, label="Filter path by terrain")
    pathselection.fields['selection'].widget.attrs['id'] = "terraintypeselection"
    fountainlist = datamng.getFountains()

    pathsformtatted = datamng.getPathsWaypoints()
    pathsbytype = datamng.getPathsByType()
    pathlenghts = datamng.getPathsLengths()
    pathslopes = datamng.getPathsSlopes()
    pathheightdiff = datamng.getPathsHeightdiffs()

    pathtypesdict = DataProcesser.listIntoDict(pathsbytype)
    pathheightdiffdict = DataProcesser.listIntoDict(pathheightdiff)
    pathslopesdict = DataProcesser.listIntoDict(pathslopes)
    pathlenghtsdict = DataProcesser.listIntoDict(pathlenghts)



    #recommendation filters
    genderchoices = [(x, x) for x in xml.getGenders()]
    genderselection = CheckBox("Select Gender")
    genderselection.fields['selection'].choices = genderchoices

    agechoices = [(x, x) for x in xml.getAgeIntervals()]
    ageintervalselection = Dropdown(label="Select age", choices=agechoices)

    heightchoices = [(x,x) for x in xml.getHeightIntervals()]
    heightselection = Dropdown(label="Select Height",choices=heightchoices)

    weightchoices = [(x,x) for x in xml.getWeightIntervals()]
    weightselection = Dropdown(label="Select Weight",choices=weightchoices)

    context = {
        'fountains': json.dumps(fountainlist),  # water fountains
        'paths': json.dumps(pathsformtatted),  # list of paths
        'pathtypes': json.dumps(pathtypesdict),  # types of paths
        'watercheckbox': waterselection,  # water fountain selection
        'pathcheckboxes': pathselection,  # checkboxes with paths
        'pathheightdiffs': pathheightdiffdict,  # dict of height differences of paths
        'pathslopes': pathslopesdict,  # dict of slopes of paths
        'pathlenghts': pathlenghtsdict,  # dict of lenghts of paths
        'gender_checkbox': genderselection,
        'age_dropdown': ageintervalselection,
        'weight_dropdown': weightselection,
        'height_dropdown': heightselection,
    }
    return HttpResponse(template.render(context, request))

def freeweight(request):
    xml = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml")
    genderchoices = [(x,x) for x in xml.getGenders()]
    genderselection = CheckBox("Select Gender")
    genderselection.fields['selection'].choices = genderchoices

    typechoices = [(x,x) for x in xml.getTrainingTypes()]
    trainingtypeselection = CheckMultiCheckBox(choices=typechoices, label="Select type of training")

    agechoices=[(x,x) for x in xml.getAgeIntervals()]
    ageintervalselection = Dropdown(label="Select age",choices=agechoices)

    heightchoices = [(x,x) for x in xml.getHeightIntervals()]
    heightselection = Dropdown(label="Select Height",choices=heightchoices)

    weightchoices = [(x,x) for x in xml.getWeightIntervals()]
    weightselection = Dropdown(label="Select Weight",choices=weightchoices)

    kcalchoices = [(x,x) for x in xml.getKcalIntervals()]
    kcalselection = Dropdown(label="Select Kcal",choices=kcalchoices)

    template = loader.get_template('park_displays_app/freeweight.html')
    context = {
        'checkbox1': genderselection,
        'dropdown1': ageintervalselection,
        'checkbox2': trainingtypeselection,
        'dropdown2': weightselection,
        'dropdown3': heightselection,
        'dropdown4': kcalselection,
    }
    return HttpResponse(template.render(context, request))
def groupfitness(request):


    template = loader.get_template('park_displays_app/groupfitness.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
def findgroups(request):
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml")
    trainingtypes=[(x,x) for x in xmlmng.getTrainingTypes()]+[('Both','Both')]
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    datamng = ParkManager("englischer_garten", xmlmng, pathtypes=path_types, gymtooltypes=gymtool_types)
    grouplist=datamng.getGroups()
    training = CheckBox("Choose type of training")
    training.fields['selection'].choices = trainingtypes
    training.fields['selection'].initial = trainingtypes

    template = loader.get_template('park_displays_app/findgroups.html')
    context = {
        'radiobuttons': training,
        'grouplist':json.dumps(grouplist),
    }
    return HttpResponse(template.render(context, request))
def grouprecommendations(request):
    template = loader.get_template('park_displays_app/grouprecommendations.html')
    xmlmng = XmlManager(
        os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "group_filters.xml")
    minmax=xmlmng.getMinMaxNumGroupFilter("num_components")
    number_of_components_list = [(str(x),str(x)) for x in range(int(minmax[0]),int(minmax[1])+1)]
    number_of_components = Dropdown("Select Number of Components")
    number_of_components.fields['selection'].choices = number_of_components_list
    number_of_components.fields['selection'].initial = number_of_components_list

    minmax = xmlmng.getMinMaxNumGroupFilter("num_males")
    number_of_males_list = [(str(x),str(x)) for x in range(int(minmax[0]),int(minmax[1])+1)]
    number_of_males = Dropdown("Select Number of Males")
    number_of_males.fields['selection'].choices = number_of_males_list
    number_of_males.fields['selection'].initial = number_of_males_list

    minmax = xmlmng.getMinMaxNumGroupFilter("num_youngs")
    number_not_adult_list = [(str(x),str(x)) for x in range(int(minmax[0]),int(minmax[1])+1)]
    number_not_adult = Dropdown("Select Number of under 18")
    number_not_adult.fields['selection'].choices = number_not_adult_list
    number_not_adult.fields['selection'].initial = number_not_adult_list

    minmax = xmlmng.getMinMaxNumGroupFilter("num_olds")
    number_of_olds_list = [(str(x),str(x)) for x in range(int(minmax[0]),int(minmax[1])+1)]
    number_of_olds = Dropdown("Select number of over 70")
    number_of_olds.fields['selection'].choices = number_of_olds_list
    number_of_olds.fields['selection'].initial = number_of_olds_list

    minmax = xmlmng.getMinMaxNumGroupFilter("averageage")
    average_age_list = [(str(x),str(x)) for x in range(int(minmax[0]),int(minmax[1])+1)]
    average_age = Dropdown("Select average age")
    average_age.fields['selection'].choices = average_age_list
    average_age.fields['selection'].initial = average_age_list

    minmax = xmlmng.getMinMaxNumGroupFilter("minage")
    minimum_age_list = [(str(x),str(x)) for x in range(int(minmax[0]),int(minmax[1])+1)]
    minimum_age = Dropdown("Select minimum age")
    minimum_age.fields['selection'].choices = minimum_age_list
    minimum_age.fields['selection'].initial = minimum_age_list

    minmax = xmlmng.getMinMaxNumGroupFilter("maxage")
    max_age_list =[(str(x),str(x)) for x in range(int(minmax[0]),int(minmax[1])+1)]
    max_age = Dropdown("Select maximum age")
    max_age.fields['selection'].choices = max_age_list
    max_age.fields['selection'].initial = max_age_list

    xmlmng = XmlManager(
        os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml")
    trainingtypes = [(x, x) for x in xmlmng.getTrainingTypes()] + [('Both', 'Both')]
    typeselection = CheckBox("Select Type")
    typeselection.fields['selection'].choices = trainingtypes
    typeselection.fields['selection'].initial = trainingtypes
    context = {
        'number_of_components':number_of_components,
        'number_of_males':number_of_males,
        'number_not_adult':number_not_adult,
        'number_of_olds':number_of_olds,
        'average_age':average_age,
        'minimum_age':minimum_age,
        'max_age':max_age,
        'typeselection':typeselection
    }
    return HttpResponse(template.render(context, request))
def startpage(request):
    template = loader.get_template('park_displays_app/startpage.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_startpage_",
    }
    return HttpResponse(template.render(context, request))
def run_walk_recommendation(request):
    template = loader.get_template('park_displays_app/run_walk_recommendation.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_run_walk_recommendation",
    }
    return HttpResponse(template.render(context, request))
def gym_recommendation(request):
    template = loader.get_template('park_displays_app/gym_recommendation.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_gym_recommendation",
    }
    return HttpResponse(template.render(context, request))
def freeweight_recommendation(request):
    template = loader.get_template('park_displays_app/freeweight_recommendation.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_freeweight_recommendation",
    }
    return HttpResponse(template.render(context, request))
def get_grouprecommendations(request):


    template = loader.get_template('park_displays_app/get_grouprecommendations.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
def path_detail(request):


    template = loader.get_template('park_displays_app/path_detail.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
