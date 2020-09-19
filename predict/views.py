from django.shortcuts import render
from .models import Match, Team, MatchResult, UserData, Prediction
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def match_date(request,date):
    permission_classes = (IsAuthenticated,) 
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
                "team_1_logo":  match.team_1.logo,
                "team_2_logo":  match.team_2.logo,
                "date": match.match_date,
                "match_credit": match.credit,
                "category": match.category.name,
            })
    else :
        data.append({"message": "No matches scheduled"})
    return JsonResponse(data,safe=False)

def match(request):
    matches = Match.objects.all();
    print(matches)
    if(matches != None):
        data = serializers.serialize('json',matches)
        return HttpResponse(data, content_type="application/json")
    else:
        return None

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
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
                "team_1_logo":  match.team_1.logo,
                "team_2_logo":  match.team_2.logo,
                "date": match.match_date,
                "match_credit": match.credit,
                "category": match.category.name,
            })
    else :
        data.append({"message": "No matches scheduled"})
    return JsonResponse(data,safe=False)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def team(request):
    teams = Team.objects.all();
    if(teams != None):
        data = serializers.serialize('json',teams)
        return HttpResponse(data, content_type="application/json")
    else:
        return None

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def result(request):
    results = MatchResult.objects.all();
    print(results)

    if(results != None):
        data = serializers.serialize('json',results)
        return HttpResponse(data, content_type="application/json")
    else:
        return None
  
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def leader_board(request):
    leaderBoard = UserData.objects.all().order_by("-points")
    if(leaderBoard != None):
        data = serializers.serialize('json',leaderBoard)
        return HttpResponse(data, content_type="application/json")
    else:
        return None

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
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
        is_draw = request.POST.get("is_draw");
        comments = request.POST.get("comments");
        
        date_predicted = now
        created_at = now
        pr = Prediction(
            date_predicted=date_predicted,
            match_id_id = match_id,
            user_id_id = user_id,
            winning_team_id = win_team_id,
            is_draw = False,
            comments = comments,
            created_at = date_predicted,
        )
        try:
            pr.save()
            values_dict = {"message" : "Success"}
            data.append(values_dict)
        except Exception as e:
            values_dict = {"message" : e}
            data.append(values_dict)
        return HttpResponse(data)

def index(request):
    return HttpResponse("Hello..")
