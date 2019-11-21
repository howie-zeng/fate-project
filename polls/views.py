from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
import os
import json

import sys
sys.path.insert(0, 'src')
from extraction import *
from write import *

dir_path = os.path.dirname(os.path.realpath(__file__))

# List of algorithms
listOfStrings = ['0g', '0gf', '0gfp', '01g', '01gf', '01gfp','05g', '05gf', '05gfp', '09g', '09gf',
                 '09gfp','p','pp','r','rp','t','tp']
# algorithm used
algorithm = ''

# user responses
# ['algorithm','query','rating','time spent']
userResponses = []

# user stats
# ['age','gender','education level','ip address', 'mturk-id']
respondent = []

def get_ip_address(request):
    """ use requestobject to fetch client machine's IP Address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', None)
    return ip


def home(request):
    #return HttpResponse(dir_path)
    return render(request, "home.html")

def demographics(request):
    if 'age' in request.GET:
        global respondent
        respondent.append(request.GET['age'])
        respondent.append(request.GET['gender'])
        respondent.append(request.GET['education'])
        respondent.append(get_ip_address(request))
        return redirect('main')
    else:
        return render(request, 'demographics.html')


def main(request):
    return render(request, "fate.html")


def end(request, num):
    global userResponses
    global respondent

    if num == "":
        # user has no responses, should enforce user to pick a choice at front end
        print("invalid num")
    else:
        userResponses = num.split()

    return redirect("thank")


def thank(request):
    if 'mturk-id' in request.GET:
        global respondent
        ID = request.GET['mturk-id']
        respondent.append(ID)
        writeToCSVFiles(respondent, userResponses,ID)

    return render(request, "end.html")


def handle(request, query):
    global algorithm
    queryResults = {}
    if query in listOfStrings:
        algorithm = query
        queryResults = extractFromFile(query + ".txt", 5)
    return JsonResponse(queryResults)
