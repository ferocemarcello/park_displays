from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
from .forms import CheckMultiCheckBox
from .forms import CheckBox
from .forms import Dropdown


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
    template = loader.get_template('park_displays_app/startpage.html')
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
    template = loader.get_template('park_displays_app/startpage.html')
    context = {
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_RUN_WALK",
    }
    return HttpResponse(template.render(context, request))
def freeweight(request):
    genderchoices = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    genderselection = CheckBox("Select Gender")
    genderselection.fields['selection'].choices = genderchoices
    genderselection.fields['selection'].initial = genderchoices

    typechoices = [('Strength', 'Strength'), ('Flexibility', 'Flexibility'), ('Both', 'Both')]
    typeselection = CheckBox("Select Type")
    typeselection.fields['selection'].choices = typechoices
    typeselection.fields['selection'].initial = typechoices

    agechoices = [('Select Age', 'Select Age'),('18 or younger', '18 or younger'), ('19-23', '19-23'), ('24-28', '24-28'), ('29-33', '29-33'), ('34-38', '34-38'), ('39-43', '39-43'), ('44-48', '44-48'), ('49+', '49+')]
    ageselection = Dropdown("Select Age")
    ageselection.fields['selection'].choices = agechoices
    ageselection.fields['selection'].initial = agechoices

    template = loader.get_template('park_displays_app/freeweight.html')
    context = {
        'checkbox1': genderselection,
        'dropdown1' : ageselection,
        'checkbox2' : typeselection,
        'context': "THIS CAPITAL STRING IS PART OF THE CONTEXT_FREEWEIGHT_EXERCISES",
    }
    return HttpResponse(template.render(context, request))

def groupfitness(request):
    template = loader.get_template('park_displays_app/groupfitness.html')
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
