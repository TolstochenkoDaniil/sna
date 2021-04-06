import random

from django.db import transaction
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from factory.django import DjangoModelFactory

from user_stats.models import UserStats


USER_NUM = 100
METHODS = ['Method1','Method2','Method3']
PERIODS = [range(x,x+5) for x in range(1,67,5)]
MULTIPLIER = random.choice(range(1,8))
ACTIVITY = [random.sample(range((30-x*random.randint(1,3)),(140-x*random.randint(5,7)),5),8) for x in range(len(PERIODS))]


class UserStatisticFactory(DjangoModelFactory):
    class Meta:
        model = UserStats


class Command(BaseCommand):
    ''''''
    help = "Generates test users data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        models = [UserStats]

        for m in models:
            m.objects.all().delete()

        users = User.objects.all()

        for i, period in enumerate(PERIODS):
            for day in period:
                for user in users:
                    activity = random.choice(ACTIVITY[i]) / 10.0
                    method = random.choice(METHODS)

                    statistic = UserStatisticFactory(
                        activity=activity,
                        period=day,
                        method=method,
                        user=user
                    )