# Generated by Django 3.1 on 2020-09-17 11:58

from django.db import migrations
category = [
    {'name':'IPL','desc':'Indian Premier League Cricket'},
    {'name':'EPL','desc':'English Premier League Football'},
    {'name':'LALIGA','desc':'Spanish Premier League Football'},
]

venues = [
    {'name':'Sharjah','desc':''},
    {'name':'Dubai','desc':''},
    {'name':'Abu Dhabi','desc':''},
]

status = [
    {'name':'Scheduled','desc':''},
    {'name':'In Progress','desc':''},
    {'name':'Completed','desc':''},
    {'name':'Abandonded','desc':''},
]
def preload_initial_data(apps,schema_editor):
    load_data(apps, schema_editor, 'Category', category)
    load_data(apps, schema_editor, 'Venue', venues)
    load_data(apps, schema_editor, 'MatchStatus', status)

def load_data(apps,schema_editor, type, data):
    categoryModel = apps.get_model('predict',type)
    for cat in data:
        m = categoryModel(**cat)
        if not categoryModel.objects.filter(name=cat['name']).exists():
            m.save()
        else:
            pass

class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(preload_initial_data),
    ]
