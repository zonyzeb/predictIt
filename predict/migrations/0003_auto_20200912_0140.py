# Generated by Django 3.1 on 2020-09-11 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0002_auto_20200912_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='team_won',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='match_team_won', to='predict.team'),
        ),
    ]
