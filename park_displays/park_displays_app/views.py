import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json

# Create your views here.
from .xmlmanager import XmlManager
from .recommendation import RunWalkRecommender,GymRecommender,GroupRecommender,FreeweightStretchingRecommender
from .data_manager import ParkManager,DataProcesser,AthleteManager
from .forms import CheckMultiCheckBox
from .forms import CheckBox
from .forms import Dropdown

app_code='--NDudeZYCPWjK333-3TxQ'
app_id='KfjYxKFR65JNn6KGSink'
path_types=XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_filters.xml").getPathTypes()
gymtool_types = XmlManager(
        os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_filters.xml").getToolTypes()
body_parts = XmlManager(
        os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml").getBodyParts()

def index(request):
    template = loader.get_template('park_displays_app/startpage.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def emergency(request):
    template = loader.get_template('park_displays_app/emergency.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_EMERGENCY",
    }
    return HttpResponse(template.render(context, request))

def runwalkrecresult(request):
    location = request.POST.get('location')
    location = location.split(',')
    location[0] = float(location[0])
    location[1] = float(location[1])
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    park = ParkManager.getParkFromLocation(location=location, xmlmanager=xmlmng)
    parkcoord = list(park[1])
    gender=""
    age=0
    weight=0
    height=0
    kcal=0

    if request.method == 'POST':
        #gender_input = CheckBox(request.POST)
        #age_input = Dropdown(request.POST)
        #weight_input = Dropdown(request.POST)
        #height_input = Dropdown(request.POST)
        #if gender_input.is_valid():
        gender_input = request.POST.getlist('selection')[0]
        #if age_input.is_valid():
        age_input = request.POST.getlist('selection')[1]
        #if weight_input.is_valid():
        weight_input = request.POST.getlist('selection')[2]
        #if height_input.is_valid():
        height_input = request.POST.getlist('selection')[3]

        kcal_input = request.POST.getlist('selection')[4]

        gender = gender_input

        if age_input == "<18":
            age = 18
        elif age_input == "18-24":
            age = 22
        elif age_input == "25-34":
            age = 30
        elif age_input == "35-44":
            age = 40
        elif age_input == "45-54":
            age = 50
        elif age_input == "55-64":
            age = 60
        elif age_input == "65-74":
            age = 70
        elif age_input == ">=75":
            age = 75

        if weight_input == "<40":
            weight = 40
        elif weight_input == "40-49 kg":
            weight = 45
        elif weight_input == "50-59 kg":
            weight = 55
        elif weight_input == "60-69 kg":
            weight = 65
        elif weight_input == "70-79 kg":
            weight = 75
        elif weight_input == "80-89 kg":
            weight = 85
        elif weight_input == "90-99 kg":
            weight = 95
        elif weight_input == "100-109 kg":
            weight = 105
        elif weight_input == "110-119 kg":
            weight = 115
        elif weight_input == ">=120":
            weight = 120

        if height_input == "<150 cm":
            height = 150
        elif height_input == "150-159 cm":
            height = 155
        elif height_input == "160-169 cm":
            height = 165
        elif height_input == "170-179 cm":
            height = 175
        elif height_input == "180-189 cm":
            height = 185
        elif height_input == "190-199 cm":
            height = 195
        elif height_input == "200-209 cm":
            height = 205
        elif height_input == ">=210 cm":
            height = 210

        if kcal_input == "<100 kcal":
            kcal = 100
        elif kcal_input == "100-499 kcal":
            kcal = 300
        elif kcal_input == "500-899 kcal":
            kcal = 700
        elif kcal_input == "900-1299 kcal":
            kcal = 1100
        elif kcal_input == "1300-1699 kcal":
            kcal = 1500
        elif kcal_input == "1700-2099 kcal":
            kcal = 1900
        elif kcal_input == "2100-2499 kcal":
            kcal = 2300
        elif kcal_input == "2500-2899 kcal":
            kcal = 2700
        elif kcal_input == ">=2900 kcal":
            kcal = 2900

    avgweekkm=40
    activity="running"
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "athletes.xml")
    shoetype=AthleteManager(0,xmlmng).getShoeType()
    recommendations=RunWalkRecommender(path_types=path_types,gender=gender,age=age,weight=weight,height=height,kcal=kcal,avgweekkm=avgweekkm,shoetype=shoetype,activity=activity).recommendPaths()#list of tuples(score, path), those have to be read and interpreted by the frontend
    template = loader.get_template('park_displays_app/run_walk_recommendation_result.html')
    context = {
        'recommendations':recommendations,
        'app_id':app_id,
        'app_code':app_code,
        'parkcoord': parkcoord,
    }
    return HttpResponse(template.render(context, request))
def freeweightrecresult(request):

    '''inputf = FormClass(None,request.POST, request.FILES)
    inputf2 = FormClass(request.POST)
    if request.method == 'POST' and inputf.is_valid() and inputf2.is_valid():
        if len(request.FILES.getlist('file_field')) == 2:
            coordinatesfile = request.FILES.getlist('file_field')[0]'''

    gender=""
    age=0
    weight=0
    height=0
    kcal=0
    gender_input = request.POST.getlist('selection')[0]
    age_input = request.POST.getlist('selection')[1]
    weight_input = request.POST.getlist('selection')[2]
    height_input = request.POST.getlist('selection')[3]
    kcal_input = request.POST.getlist('selection')[4]

    gender = gender_input

    if age_input == "<18":
        age = 18
    elif age_input == "18-24":
        age = 22
    elif age_input == "25-34":
        age = 30
    elif age_input == "35-44":
        age = 40
    elif age_input == "45-54":
        age = 50
    elif age_input == "55-64":
        age = 60
    elif age_input == "65-74":
        age = 70
    elif age_input == ">=75":
        age = 75

    if weight_input == "<40":
        weight = 40
    elif weight_input == "40-49 kg":
        weight = 45
    elif weight_input == "50-59 kg":
        weight = 55
    elif weight_input == "60-69 kg":
        weight = 65
    elif weight_input == "70-79 kg":
        weight = 75
    elif weight_input == "80-89 kg":
        weight = 85
    elif weight_input == "90-99 kg":
        weight = 95
    elif weight_input == "100-109 kg":
        weight = 105
    elif weight_input == "110-119 kg":
        weight = 115
    elif weight_input == ">=120":
        weight = 120

    if height_input == "<150 cm":
        height = 150
    elif height_input == "150-159 cm":
        height = 155
    elif height_input == "160-169 cm":
        height = 165
    elif height_input == "170-179 cm":
        height = 175
    elif height_input == "180-189 cm":
        height = 185
    elif height_input == "190-199 cm":
        height = 195
    elif height_input == "200-209 cm":
        height = 205
    elif height_input == ">=210 cm":
        height = 210

    if kcal_input == "<100":
        kcal = 100
    elif kcal_input == "100-499":
        kcal = 300
    elif kcal_input == "500-899":
        kcal = 700
    elif kcal_input == "900-1299":
        kcal = 1100
    elif kcal_input == "1300-1699":
        kcal = 1500
    elif kcal_input == "1700-2099":
        kcal = 1900
    elif kcal_input == "2100-2499":
        kcal = 2300
    elif kcal_input == "2500-2899":
        kcal = 2700
    elif kcal_input == ">=2900":
        kcal = 2900

    intensity=60#0-100
    exercises=FreeweightStretchingRecommender(gender=gender,age=age,weight=weight,height=height,kcal=kcal,intensity=intensity,freeweight=True,stretching=True).recommendExercises()
    template = loader.get_template('park_displays_app/freeweight_recommendation_result.html')
    context = {
        'exercises': exercises,
    }
    return HttpResponse(template.render(context, request))
def gymrecresult(request):

    '''inputf = FormClass(None,request.POST, request.FILES)
    inputf2 = FormClass(request.POST)
    if request.method == 'POST' and inputf.is_valid() and inputf2.is_valid():
        if len(request.FILES.getlist('file_field')) == 2:
            coordinatesfile = request.FILES.getlist('file_field')[0]'''

    location = request.POST.get('location')
    location = location.split(',')
    location[0] = float(location[0])
    location[1] = float(location[1])
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    park = ParkManager.getParkFromLocation(location=location, xmlmanager=xmlmng)
    parkname = park[0]
    parkcoord = list(park[1])
    gender = ""
    age = 0
    weight = 0
    height = 0
    kcal = 0
    gender_input = request.POST.getlist('selection')[0]
    age_input = request.POST.getlist('selection')[1]
    weight_input = request.POST.getlist('selection')[2]
    height_input = request.POST.getlist('selection')[3]
    kcal_input = request.POST.getlist('selection')[4]

    gender = gender_input

    if age_input == "<18":
        age = 18
    elif age_input == "18-24":
        age = 22
    elif age_input == "25-34":
        age = 30
    elif age_input == "35-44":
        age = 40
    elif age_input == "45-54":
        age = 50
    elif age_input == "55-64":
        age = 60
    elif age_input == "65-74":
        age = 70
    elif age_input == ">=75":
        age = 75

    if weight_input == "<40":
        weight = 40
    elif weight_input == "40-49 kg":
        weight = 45
    elif weight_input == "50-59 kg":
        weight = 55
    elif weight_input == "60-69 kg":
        weight = 65
    elif weight_input == "70-79 kg":
        weight = 75
    elif weight_input == "80-89 kg":
        weight = 85
    elif weight_input == "90-99 kg":
        weight = 95
    elif weight_input == "100-109 kg":
        weight = 105
    elif weight_input == "110-119 kg":
        weight = 115
    elif weight_input == ">=120":
        weight = 120

    if height_input == "<150 cm":
        height = 150
    elif height_input == "150-159 cm":
        height = 155
    elif height_input == "160-169 cm":
        height = 165
    elif height_input == "170-179 cm":
        height = 175
    elif height_input == "180-189 cm":
        height = 185
    elif height_input == "190-199 cm":
        height = 195
    elif height_input == "200-209 cm":
        height = 205
    elif height_input == ">=210 cm":
        height = 210

    if kcal_input == "<100":
        kcal = 100
    elif kcal_input == "100-499":
        kcal = 300
    elif kcal_input == "500-899":
        kcal = 700
    elif kcal_input == "900-1299":
        kcal = 1100
    elif kcal_input == "1300-1699":
        kcal = 1500
    elif kcal_input == "1700-2099":
        kcal = 1900
    elif kcal_input == "2100-2499":
        kcal = 2300
    elif kcal_input == "2500-2899":
        kcal = 2700
    elif kcal_input == ">=2900":
        kcal = 2900
        
    bodyparts=body_parts
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    gymtools=ParkManager(parkname,xmlmng,path_types,gymtool_types).getGymTools()
    gymtool_scores = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "gymtool_bodypart.xml").getGymToolsScore()
    recommendation=GymRecommender(gender=gender,age=age,weight=weight,height=height,kcal=kcal,bodyparts=bodyparts,machines=gymtools,gymtool_scores=gymtool_scores).recommendActivities()
    template = loader.get_template('park_displays_app/gym_recommendation_result.html')
    context = {
        'recommendation':recommendation,
        'parkcoord': parkcoord,
    }
    return HttpResponse(template.render(context, request))

def grouprecresult(request):
    template = loader.get_template('park_displays_app/group_recommendation_result.html')

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
    gender="male"
    numcomponents=10
    nummales=4
    numunder18=3
    numover70=1
    avgage=40
    minage=17
    maxage=72
    kcal=500
    intensity=60#0-100
    exercises = GroupRecommender(numcomponents=numcomponents, nummales=nummales, numunder18=numunder18, numover70=numover70, avgage=avgage,minage=minage,maxage=maxage,kcal=kcal,stretching=True, freeweight=True,intensity=intensity).recommendExercises()
    context = {
        'number_of_components':number_of_components,
        'number_of_males':number_of_males,
        'number_not_adult':number_not_adult,
        'number_of_olds':number_of_olds,
        'average_age':average_age,
        'minimum_age':minimum_age,
        'max_age':max_age,
        'typeselection':typeselection,
        'exercises':exercises
    }
    return HttpResponse(template.render(context, request))

def sportrec(request):
    template = loader.get_template('park_displays_app/run_walk_recommendation.html')
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
    location = request.POST.get('location')
    location = location.split(',')
    location[0] = float(location[0])
    location[1] = float(location[1])
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    park = ParkManager.getParkFromLocation(location=location, xmlmanager=xmlmng)
    parkname = park[0]
    parkcoord = list(park[1])
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    datamng = ParkManager(parkname, xmlmng, pathtypes=path_types, gymtooltypes=gymtool_types)
    runners=datamng.getRunners()
    walkers=datamng.getWalkers()
    gymathletes=datamng.getGymAthletes()
    freeweightathletes=datamng.getFreeweightAthletes()
    stretchers = datamng.getStretchers()

    activityselection = Dropdown(label="Select Activity", choices=[('Running','Running'), ('Walking','Walking'), ('Outdoor Gym','Outdoor Gym'), ('Freeweight','Freeweight'), ('Stretching','Stretching')])

    template = loader.get_template('park_displays_app/similarusers.html')
    context = {
        'runners':json.dumps(runners),
        'walkers':json.dumps(walkers),
        'gymathletes':json.dumps(gymathletes),
        'freeweightathletes':json.dumps(freeweightathletes),
        'stretchers':json.dumps(stretchers),
        'app_id':app_id,
        'app_code':app_code,
        'activity_filter': activityselection,
        'parkcoord':parkcoord,
    }
    return HttpResponse(template.render(context, request))
def outdoorgym(request):
    location = request.POST.get('location')
    location = location.split(',')
    return HttpResponse("location[0]=%s." % location[0])
    location[0] = float(location[0])
    location[1] = float(location[1])
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    park = ParkManager.getParkFromLocation(location=location, xmlmanager=xmlmng)
    parkname = park[0]
    parkcoord = list(park[1])
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    xml = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml")
    datamng = ParkManager(parkname, xmlmng,pathtypes=path_types, gymtooltypes=gymtool_types)
    choices=[(x[0],x[0]) for x in datamng.getGymTools()]
    gymselectionmulticheck = CheckMultiCheckBox(choices=choices,label="Select Gym tools to show")
    template = loader.get_template('park_displays_app/outdoorgym.html')
    gymtools=datamng.getGymTools()
    gymtoolscoordinates=[]
    for gymtool in gymtools:
        gymtoolscoordinates.append(gymtool[1])
    gymtoolsbytype = datamng.getGymToolsByType()
    gymtoolsbytypedict = DataProcesser.listIntoDict(gymtoolsbytype)

    #recommendation filters
    genderchoices = [(x, x) for x in xml.getGenders()]
    genderselection = CheckBox("Select Gender")
    genderselection.fields['selection'].choices = genderchoices

    agechoices = [(x, x) for x in xml.getAgeIntervals()]
    ageintervalselection = Dropdown(label="Age", choices=[('', "Select Age")] + agechoices)

    heightchoices = [(x,x) for x in xml.getHeightIntervals()]
    heightselection = Dropdown(label="Height",choices=[('', "Select Height")] + heightchoices)

    weightchoices = [(x,x) for x in xml.getWeightIntervals()]
    weightselection = Dropdown(label="Weight",choices=[('', "Select Weight")] + weightchoices)

    kcalchoices = [(x,x) for x in xml.getKcalIntervals()]
    kcalselection = Dropdown(label="Kcal",choices=[('', "Select Kcal")] + kcalchoices)

    context = {
        'gymtoolscoordinates':json.dumps(gymtoolscoordinates),
        'gymtoolsbytype':json.dumps(gymtoolsbytypedict),
        'checkboxes': gymselectionmulticheck,
        'gymtooltypes': gymtool_types,
        'gender_checkbox': genderselection,
        'age_dropdown': ageintervalselection,
        'weight_dropdown': weightselection,
        'height_dropdown': heightselection,
        'kcal_dropdown': kcalselection,
        'app_id':app_id,
        'app_code':app_code,
        'parkcoord': parkcoord,
    }
    return HttpResponse(template.render(context, request))

def parkdetails(request):
    location = request.POST.get('location')
    location = location.split(',')
    location[0] = float(location[0])
    location[1] = float(location[1])
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    park = ParkManager.getParkFromLocation(location=location, xmlmanager=xmlmng)
    parkname = park[0]
    parkcoord = list(park[1])
    template = loader.get_template('park_displays_app/parkdetails.html')
    xmlmng=XmlManager(os.path.dirname(os.path.realpath(__file__))+os.sep+"xmldata"+os.sep+"park_data.xml")
    datamng = ParkManager(parkname, xmlmng, pathtypes=path_types, gymtooltypes=gymtool_types)
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
        'app_id':app_id,
        'app_code':app_code,
        'parkcoord': parkcoord,
    }
    return HttpResponse(template.render(context, request))

def runwalk(request):
    location=request.POST.get('location')
    location = location.split(',')
    location[0] = float(location[0])
    location[1] = float(location[1])
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    park = ParkManager.getParkFromLocation(location=location, xmlmanager=xmlmng)
    parkname = park[0]
    parkcoord = list(park[1])
    xml = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml")

    template = loader.get_template('park_displays_app/run_walk.html')
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    datamng = ParkManager(parkname, xmlmng, pathtypes=path_types, gymtooltypes=gymtool_types)
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
    genderselection = CheckBox("Gender")
    genderselection.fields['selection'].choices = genderchoices

    agechoices = [(x, x) for x in xml.getAgeIntervals()]
    ageintervalselection = Dropdown(label="Age", choices=[('', "Select Age")] + agechoices)

    heightchoices = [(x,x) for x in xml.getHeightIntervals()]
    heightselection = Dropdown(label="Height",choices=[('', "Select Height")] + heightchoices)

    weightchoices = [(x,x) for x in xml.getWeightIntervals()]
    weightselection = Dropdown(label="Weight",choices=[('', "Select Weight")] + weightchoices)

    kcalchoices = [(x,x) for x in xml.getKcalIntervals()]
    kcalselection = Dropdown(label="Kcal",choices=[('', "Select Kcal")] + kcalchoices)

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
        'kcal_dropdown': kcalselection,
        'app_id':app_id,
        'app_code':app_code,
        'parkcoord': parkcoord,
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
    ageintervalselection = Dropdown(label="Age",choices=[('', "Select Age")] + agechoices)

    heightchoices = [(x,x) for x in xml.getHeightIntervals()]
    heightselection = Dropdown(label="Height",choices=[('', "Select Height")] + heightchoices)

    weightchoices = [(x,x) for x in xml.getWeightIntervals()]
    weightselection = Dropdown(label="Weight",choices=[('', "Select Weight")] + weightchoices)

    kcalchoices = [(x,x) for x in xml.getKcalIntervals()]
    kcalselection = Dropdown(label="Kcal",choices=[('', "Select Kcal")] + kcalchoices)

    template = loader.get_template('park_displays_app/freeweight.html')
    context = {
        'gender_checkbox': genderselection,
        'age_dropdown': ageintervalselection,
        'training_type_checkbox': trainingtypeselection,
        'weight_dropdown': weightselection,
        'height_dropdown': heightselection,
        'kcal_dropdown': kcalselection,
    }
    return HttpResponse(template.render(context, request))
def groupfitness(request):
    xml = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml")

    template = loader.get_template('park_displays_app/groupfitness.html')

    #recommendation filters
    genderchoices = [(x, x) for x in xml.getGenders()]
    genderselection = CheckBox("Select Gender")
    genderselection.fields['selection'].choices = genderchoices

    agechoices = [(x, x) for x in xml.getAgeIntervals()]
    ageintervalselection = Dropdown(label="Age", choices=[('', "Select Age")] + agechoices)

    heightchoices = [(x,x) for x in xml.getHeightIntervals()]
    heightselection = Dropdown(label="Height",choices=[('', "Select Height")] + heightchoices)

    weightchoices = [(x,x) for x in xml.getWeightIntervals()]
    weightselection = Dropdown(label="Weight",choices=[('', "Select Weight")] + weightchoices)

    context = {
        'gender_checkbox': genderselection,
        'age_dropdown': ageintervalselection,
        'weight_dropdown': weightselection,
        'height_dropdown': heightselection,
    }
    return HttpResponse(template.render(context, request))
def findgroups(request):
    location = request.POST.get('location')
    location = location.split(',')
    location[0] = float(location[0])
    location[1] = float(location[1])
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    park = ParkManager.getParkFromLocation(location=location, xmlmanager=xmlmng)
    parkname = park[0]
    parkcoord = list(park[1])
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "athlete_filters.xml")
    trainingtypes=[(x,x) for x in xmlmng.getTrainingTypes()]+[('Both','Both')]
    xmlmng = XmlManager(os.path.dirname(os.path.realpath(__file__)) + os.sep + "xmldata" + os.sep + "park_data.xml")
    datamng = ParkManager(parkname, xmlmng, pathtypes=path_types, gymtooltypes=gymtool_types)
    grouplist=datamng.getGroups()
    training = CheckBox("Choose type of training")
    training.fields['selection'].choices = trainingtypes
    training.fields['selection'].initial = trainingtypes

    template = loader.get_template('park_displays_app/findgroups.html')
    context = {
        'radiobuttons': training,
        'grouplist':json.dumps(grouplist),
        'app_id':app_id,
        'app_code': app_code,
        'parkcoord': parkcoord,
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
        'app_id':app_id,
        'app_code':app_code,
    }
    return HttpResponse(template.render(context, request))
def gym_recommendation(request):
    template = loader.get_template('park_displays_app/gym_recommendation_result.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_gym_recommendation",
        'app_id': app_id,
        'app_code':app_code,
    }
    return HttpResponse(template.render(context, request))
def freeweight_recommendation(request):
    template = loader.get_template('park_displays_app/freeweight_recommendation_result.html')
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
