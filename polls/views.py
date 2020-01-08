from django.shortcuts import render
from django.shortcuts import redirect
from polls.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
import os
import json

import sys
sys.path.insert(0, './src')
from extraction import *
from write import *

dir_path = os.path.dirname(os.path.realpath(__file__))

# List of algorithms
listOfStrings = ['0g', '03gfp', '05gfp', '09gfp']
# algorithm used
algorithm = ''

# user responses
# ['algorithm','query','rating','time spent']
userResponses = []

# user stats
# ['age','gender','education level','ip address', 'browser-info', 'mturk-id']
respondent = []


def get_ip_address(request):
    """ use requestobject to fetch client machine's IP Address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', None)
    return ip


def get_browser_info(request):
    browser_info = request.user_agent.os.family + " " + request.user_agent.browser.family + " "
    if request.user_agent.is_pc:
        browser_info += "PC"
    else:
        browser_info += "Mobile"
    return browser_info


def home(request):
    #return HttpResponse(dir_path)
    return render(request, "home.html")


def demographics(request):
    if 'age' in request.GET:
        global respondent
        respondent.clear()
        respondent.append(request.GET['age'])
        respondent.append(request.GET['gender'])
        respondent.append(request.GET['education'])
        respondent.append(get_ip_address(request))
        respondent.append(get_browser_info(request))
        return redirect('instructions')
    else:
        return render(request, 'demographics.html')


def instructions(request):
    return render(request, 'instructions.html')


def main(request):
    return render(request, "fate.html")


def end(request, num):
    global userResponses

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
        write(ID)

    return render(request, "end.html")


def handle(request, query):
    global algorithm
    queryResults = {}
    if query in listOfStrings:
        algorithm = query
        queryResults = extractFromFile(query + ".txt", 5)
    return JsonResponse(queryResults)


def write(user_id):
    global userResponses
    global respondent

    # check length, if doesn't match, quit
    # comment out the following code during testing
    if len(respondent) != 6:
        print("Respondent data misMatch. Expected: 6, Given: " + str(len(respondent)))
        return

    if len(userResponses) != 160:
        print("Rating data misMatch. Expected: 160, Given: " + str(len(userResponses)))
        return

    # writeToCSVFiles(respondent, userResponses,ID)

    # ['age','gender','education level','ip address', 'browser-info', 'mturk-id']
    user = UserInfo(mturk_id=user_id,
                    ip_address=respondent[3],
                    browser_info=respondent[4],
                    age=respondent[0],
                    gender=respondent[1],
                    education=respondent[2])
    user.save()

    # ['algorithm','query','rating','time spent']
    userResponses = [userResponses[x:x + 4] for x in range(0, len(userResponses), 4)]
    for i in range(40):
        current = userResponses[i]
        response = Response(mturk_id=user_id,
                            algorithm=current[0],
                            query=current[1],
                            rating=current[2],
                            time_spent=current[3])
        response.save()
