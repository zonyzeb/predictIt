from django.shortcuts import render
from .models import Match, Team, MatchResult, UserData, Prediction
# from .models import Team
# from .models import MatchResult
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

from django.http import HttpResponse
import datetime

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
# def match_date_archive(request,year,month,date):
#     from datetime import datetime
#     dateval = datetime.strptime(f'{year}-{month}-{date}', '%Y-%m-%d').date()
#     print ("=====")
#     print (dateval)
#     print ("=====")
#     matches = Match.objects.filter(match_date=dateval)
#     data = serializers.serialize('json',matches)
#     # return HttpResponse(matches)
#     return HttpResponse(data, content_type="application/json")

def match_date(request,date):
    from datetime import datetime
    dateval = datetime.strptime(date, "%Y-%m-%d").date()
    matches = Match.objects.filter(match_date=dateval)
    data = []
    if len(matches) > 0 :
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
    else :
        data.append({"message": "No matches scheduled"})
    return JsonResponse(data,safe=False)

def match_upcoming(request):
    matches = Match.objects.filter(status__name='Scheduled')
    data = []
    if len(matches) > 0 :
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
    else :
        data.append({"message": "No matches scheduled"})
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

def leader_board(request):
    leaderBoard = UserData.objects.all().order_by("-points")
    if(leaderBoard != None):
        data = serializers.serialize('json',leaderBoard)
       # return HttpResponse(matches)
        return HttpResponse(data, content_type="application/json")
    else:
        return None
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def match_predict(request):
    now = datetime.datetime.now()
    data = []
    values_dict = {}
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        user_id = request.POST.get("user_id");
        match_id = request.POST.get("match_id");
        win_team_id = request.POST.get("win_team_id");
       # loss_team_id = request.POST.get("");
        is_draw = request.POST.get("is_draw");
        comments = request.POST.get("comments");
        
        date_predicted = now
        created_at = now
        pr = Prediction(
            date_predicted=date_predicted,
            match_id_id = match_id,
            user_id_id = user_id,
            winning_team_id = win_team_id,
            #loosing_team_id = 2,
            is_draw = False,
            comments = comments,
            created_at = date_predicted,
        )
        pr.save()
        
        # predictModel = apps.get_model('predict',Prediction)
        # m = categoryModel(**cat)
        data.append(values_dict)
        #data = serializers.serialize('json',vals)
        return HttpResponse(data)

def year_archive(request,year):
    return HttpResponse("Hello1..")

def index(request):
    return HttpResponse("Hello..")