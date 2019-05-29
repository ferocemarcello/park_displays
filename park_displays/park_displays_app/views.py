from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_INDEX",
    }
    return HttpResponse(template.render(context, request))
def emergency(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_EMERGENCY",
    }
    return HttpResponse(template.render(context, request))
def weather(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_WEATHER",
    }
    return HttpResponse(template.render(context, request))
def sportrec(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_SPORT_REC",
    }
    return HttpResponse(template.render(context, request))
def parkdetails(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_PARK_DETAILS",
    }
    return HttpResponse(template.render(context, request))
def social(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_SOCIAL",
    }
    return HttpResponse(template.render(context, request))
def login(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_LOGIN",
    }
    return HttpResponse(template.render(context, request))
def similarusers(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_SIMILAR_USERS",
    }
    return HttpResponse(template.render(context, request))
def outdoorgym(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_OUTDOOR_GYM",
    }
    return HttpResponse(template.render(context, request))
def runwalk(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_RUN_WALK",
    }
    return HttpResponse(template.render(context, request))
def freeweight(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_FREEWEIGHT_EXERCISES",
    }

def freeweight(request):
    template = loader.get_template('park_displays_app/index.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_OUTDOOR_FITNESS",
    }
    return HttpResponse(template.render(context, request))
