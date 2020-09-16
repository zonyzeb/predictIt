from django.shortcuts import render
from .models import Match
from .models import Team
from .models import MatchResult
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

from django.http import HttpResponse
# Create your views here.
def match(request):
    matches = Match.objects.all();
    print(matches)

    if(matches != None):
        data = serializers.serialize('json',matches)
       # return HttpResponse(matches)
        return HttpResponse(data, content_type="application/json")
    else:
        return None
    #return render(request,'match.html',{'matches': matches})
def match_date_archive(request,year,month,date):
    from datetime import datetime
    dateval = datetime.strptime(f'{year}-{month}-{date}', '%Y-%m-%d').date()
    print ("=====")
    print (dateval)
    print ("=====")
    matches = Match.objects.filter(match_date=dateval)
    data = serializers.serialize('json',matches)
    # return HttpResponse(matches)
    return HttpResponse(data, content_type="application/json")

def match_date(request,date):
    from datetime import datetime
    dateval = datetime.strptime(date, "%Y-%m-%d").date()
    
    #dateval = datetime.strptime(f'{date}', '%Y-%m-%d').date()
    print ("=====")
    print (dateval)
    print ("=====")
    matches = Match.objects.filter(match_date=dateval)
    data = []
    for match in matches:
        
        data.append({
            "match_name": match.name,
            "desc":  match.desc,
            "team_1":  match.team_1.name,
            "team_2":  match.team_2.name,
            "date": match.match_date,
            "match_credit": match.credit,
            "category": match.category.name,
        })
    print(type(matches))
    # data = serializers.serialize('json',data)


    # return HttpResponse(matches)
    return JsonResponse(data,safe=False)

def team(request):
    teams = Team.objects.all();
    print(teams)

    if(teams != None):
        data = serializers.serialize('json',teams)
       # return HttpResponse(matches)
        return HttpResponse(data, content_type="application/json")
    else:
        return None
    #return render(request,'match.html',{'matches': matches})


def result(request):
    results = MatchResult.objects.all();
    print(results)

    if(results != None):
        data = serializers.serialize('json',results)
       # return HttpResponse(matches)
        return HttpResponse(data, content_type="application/json")
    else:
        return None
    #return render(request,'match.html',{'matches': matches})

def year_archive(request,year):
    return HttpResponse("Hello1..")

def index(request):
    return HttpResponse("Hello..")