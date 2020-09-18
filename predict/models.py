from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    logo = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class MatchStatus(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    point = models.IntegerField()
    desc =  models.TextField()
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    logo = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class Match(models.Model):
    name = models.CharField(max_length=100)
    desc =  models.TextField()
    venue =  models.ForeignKey(Venue,on_delete=models.CASCADE, default=1)
    match_date = models.DateField()
    status = models.ForeignKey(MatchStatus, on_delete=models.CASCADE)
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_2 = models.ForeignKey(Team, related_name='%(class)s_team2',on_delete=models.CASCADE)
    credit = models.IntegerField(default=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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
    winning_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # loosing_team = models.ForeignKey(Team, related_name='%(class)s_loosing',on_delete=models.CASCADE)
    is_draw = models.BooleanField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

class UserData(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    points = models.BigIntegerField(default=0)
    credits = models.BigIntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    
    