from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
from .forms import CheckMultiCheckBox


def index(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {

        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_INDEX",
    }
    return HttpResponse(template.render(context, request))
def emergency(request):
    template = loader.get_template('park_displays_app/startpage.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_EMERGENCY",
    }
    return HttpResponse(template.render(context, request))
def weather(request):
    template = loader.get_template('park_displays_app/startpage.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_WEATHER",
    }
    return HttpResponse(template.render(context, request))
def sportrec(request):
    template = loader.get_template('park_displays_app/recommendation.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_SPORT_REC",
    }
    return HttpResponse(template.render(context, request))
def parkdetails(request):
    template = loader.get_template('park_displays_app/startpage.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_PARK_DETAILS",
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
    template = loader.get_template('park_displays_app/startpage.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_SIMILAR_USERS",
    }
    return HttpResponse(template.render(context, request))
def outdoorgym(request):
    choices=[('a','a'), ('b','b'),('c','c'),('d','d')]
    gymselectionmulticheck = CheckMultiCheckBox("Select Gym tools to show")
    gymselectionmulticheck.fields['gymselection'].choices = choices
    gymselectionmulticheck.fields['gymselection'].initial = choices
    template = loader.get_template('park_displays_app/outdoorgym.html')
    context = {
        'checkboxes': gymselectionmulticheck,
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_OUTDOOR_GYM",
    }
    return HttpResponse(template.render(context, request))
def runwalk(request):
    template = loader.get_template('park_displays_app/run_walk.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_RUN_WALK",
    }
    return HttpResponse(template.render(context, request))
def freeweight(request):
    template = loader.get_template('park_displays_app/startpage.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_FREEWEIGHT_EXERCISES",
    }
    return HttpResponse(template.render(context, request))

def groupfitness(request):
    template = loader.get_template('park_displays_app/startpage.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_groupfitness",
    }
    return HttpResponse(template.render(context, request))

def findgroups(request):
    template = loader.get_template('park_displays_app/findgroups.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_findgroups",
    }
    return HttpResponse(template.render(context, request))

def grouprecommendations(request):
    template = loader.get_template('park_displays_app/grouprecommendations.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_grouprecommendations",
    }
    return HttpResponse(template.render(context, request))
def startpage(request):
    template = loader.get_template('park_displays_app/startpage.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_startpage_",
    }
    return HttpResponse(template.render(context, request))
