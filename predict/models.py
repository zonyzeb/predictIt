from django.db import models

# Create your models here.
from django.conf import settings

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField()
    point = models.IntegerField()
    desc =  models.TextField()
    category = models.IntegerField(default=1)
    logo = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.name


class Match(models.Model):
    name = models.CharField(max_length=100)
    desc =  models.TextField()
    match_date = models.DateField()
    status = models.IntegerField()
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE)
    #team_2 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_2 = models.ForeignKey(Team, related_name='%(class)s_team2',on_delete=models.CASCADE)
    credit = models.IntegerField(default=100)
    category = models.IntegerField(default=1)
    def __str__(self):
        return self.name

class MatchResult(models.Model):
    match_id =  models.ForeignKey(Match, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    score =  models.TextField(blank=True, null=True)
    has_won = models.BooleanField()
    has_lost = models.BooleanField()
    is_draw = models.BooleanField()

class Prediction(models.Model):
    date_predicted = models.DateField()
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.IntegerField()
  
    
    