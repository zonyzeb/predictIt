# Generated by Django 3.1 on 2020-09-12 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0003_auto_20200912_0140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='date_played',
            new_name='match_date',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team_won',
        ),
        migrations.AddField(
            model_name='match',
            name='category',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='match',
            name='credit',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='team',
            name='category',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='MatchResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.TextField(blank=True, null=True)),
                ('has_won', models.BooleanField()),
                ('has_lost', models.BooleanField()),
                ('is_draw', models.BooleanField()),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predict.match')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predict.team')),
            ],
        ),
    ]
