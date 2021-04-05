import factory
from factory.django import DjangoModelFactory

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction


NUM_USERS = 100


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    email = factory.Faker('email')
    is_active = True


class Command(BaseCommand):
    ''''''
    help = "Generates test users"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        models = [User]

        for m in models:
            m.objects.all().delete()

        for _ in range(NUM_USERS):
            user = UserFactory.create()