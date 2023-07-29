#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import member

# Create your views here.

def members(request):
    mymembers = member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymembers,
    }
    #template = loader.get_template('myfirst.html')
    #return HttpResponse(template.render())
    return HttpResponse(template.render(context,request))
    #return HttpResponse("Hello world!")

def details(request, id):
    mymember = member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))
    '''The details view does the following:
    Gets the id as an argument.
    Uses the id to locate the correct record in the Member table.
    loads the details.html template.
    Creates an object containing the member.
    Sends the object to the template.
    Outputs the HTML that is rendered by the template.'''

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
    '''
    loads the main.html template.
    Outputs the HTML that is rendered by the template.'''

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits' : ['Apple','Banana','Cherry']
    }
    return HttpResponse(template.render(context, request))


