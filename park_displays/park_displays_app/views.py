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
    genderchoices = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    genderselection = CheckBox("Select Gender")
    genderselection.fields['selection'].choices = genderchoices
    genderselection.fields['selection'].initial = genderchoices

    typechoices = [('Strength', 'Strength'), ('Flexibility', 'Flexibility'), ('Both', 'Both')]
    typeselection = CheckBox("Select Type")
    typeselection.fields['selection'].choices = typechoices
    typeselection.fields['selection'].initial = typechoices

    agechoices = [('Select Age', 'Select Age'), ('18 or younger', '18 or younger'), ('19-23', '19-23'),
                  ('24-28', '24-28'), ('29-33', '29-33'), ('34-38', '34-38'), ('39-43', '39-43'), ('44-48', '44-48'),
                  ('49+', '49+')]
    ageselection = Dropdown("Select Age")
    ageselection.fields['selection'].choices = agechoices
    ageselection.fields['selection'].initial = agechoices

    heightchoices = [('Select Height', 'Select Height'), ('<150', '<150'), ('150-160', '150-160'),
                  ('161-170', '161-170'), ('171-180', '171-180'), ('181-190', '181-190'), ('191-200', '191-200'), ('>200', '>200')]
    heightselection = Dropdown("Select Height")
    heightselection.fields['selection'].choices = heightchoices
    heightselection.fields['selection'].initial = heightchoices

    weightchoices = [('Select Weight', 'Select Weight'), ('<50', '<50'), ('50-59', '50-59'),
                  ('60-69', '60-69'), ('70-79', '70-79'), ('80-89', '80-89'), ('90-99', '90-99'), ('100-109', '100-109'),
                  ('>110', '>110')]
    weightselection = Dropdown("Select Age")
    weightselection.fields['selection'].choices = weightchoices
    weightselection.fields['selection'].initial = weightchoices

    kcalchoices = [('Select Kcal', 'Select Kcal'), ('<100', '<100'), ('100-200', '100-200'),
                     ('200-300', '200-300'), ('300-400', '300-400'), ('400-500', '400-500'), ('500-600', '500-600'),
                     ('600-700', '600-700'), ('>700', '>700')]
    kcalselection = Dropdown("Select Kcal")
    kcalselection.fields['selection'].choices = kcalchoices
    kcalselection.fields['selection'].initial = kcalchoices

    template = loader.get_template('park_displays_app/freeweight.html')
    context = {
        'checkbox1': genderselection,
        'dropdown1' : ageselection,
        'checkbox2' : typeselection,
        'dropdown2' : weightselection,
        'dropdown3': heightselection,
        'dropdown4': kcalselection,
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
