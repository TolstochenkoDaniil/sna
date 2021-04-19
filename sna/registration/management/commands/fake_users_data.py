import itertools
import random

from django.db import transaction
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from factory.django import DjangoModelFactory

from user_stats.models import UserStats


USER_NUM = 100
METHODS = ['Timer','Disable notifications','Deny app access']
PERIODS = [range(x,x+5) for x in range(1,30,5)]
MULTIPLIER = random.choice(range(1,8))
ACTIVITY = (range((30-x*random.randint(1,4)),(70-x*random.randint(2,10)),1) for x in range(len(PERIODS)))


class UserStatisticFactory(DjangoModelFactory):
    class Meta:
        model = UserStats


class Command(BaseCommand):
    help = "Generates test users data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        models = [UserStats]

        for m in models:
            m.objects.all().delete()

        users = User.objects.all()

        for period in PERIODS:
            activity_list = next(ACTIVITY)

            for day in period:
                for user, method in zip(users, itertools.cycle(METHODS)):
                    activity = random.choice(activity_list) / 10.0

                    statistic = UserStatisticFactory(
                        activity=activity,
                        period=day,
                        method=method,
                        user=user
                    )