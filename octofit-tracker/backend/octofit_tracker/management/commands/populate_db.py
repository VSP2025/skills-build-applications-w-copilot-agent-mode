from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create users (superheroes)
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'first_name': 'Tony', 'last_name': 'Stark'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'first_name': 'Steve', 'last_name': 'Rogers'},
            {'username': 'spiderman', 'email': 'spidey@marvel.com', 'first_name': 'Peter', 'last_name': 'Parker'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com', 'first_name': 'Bruce', 'last_name': 'Wayne'},
            {'username': 'superman', 'email': 'superman@dc.com', 'first_name': 'Clark', 'last_name': 'Kent'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'first_name': 'Diana', 'last_name': 'Prince'},
        ]
        marvel_users = [User.objects.create(**hero) for hero in marvel_heroes]
        dc_users = [User.objects.create(**hero) for hero in dc_heroes]

        # Create teams
        marvel_team = Team.objects.create(name='Team Marvel')
        marvel_team.members.set(marvel_users)
        dc_team = Team.objects.create(name='Team DC')
        dc_team.members.set(dc_users)

        # Create workouts
        workout1 = Workout.objects.create(name='Push Ups', description='Upper body strength', difficulty='Easy')
        workout2 = Workout.objects.create(name='Running', description='Cardio endurance', difficulty='Medium')
        workout3 = Workout.objects.create(name='Deadlift', description='Full body strength', difficulty='Hard')

        # Create activities
        Activity.objects.create(user=marvel_users[0], activity_type='Push Ups', duration=30, calories_burned=200, date='2023-01-01')
        Activity.objects.create(user=dc_users[0], activity_type='Running', duration=45, calories_burned=400, date='2023-01-02')
        Activity.objects.create(user=marvel_users[1], activity_type='Deadlift', duration=60, calories_burned=600, date='2023-01-03')

        # Create leaderboards
        Leaderboard.objects.create(team=marvel_team, score=1200)
        Leaderboard.objects.create(team=dc_team, score=1100)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
