from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class UserStats(models.Model):
    '''
    Model represents user inputed statistic
    about his social activity over period
    '''
    class SNAMethod(models.TextChoices):
        '''
        Class with method of preventing social network addiction names
        '''
        METHOD1 = 'MT1', ('Method_1')
        METHOD2 = 'MT2', ('Method_2')
        METHOD3 = 'MT3', ('Method_3')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.FloatField(
        error_messages={
            'blank': 'This field cannot be blank'
        }
    )
    period = models.IntegerField(
        validators=[
            MinValueValidator(limit_value=1, message='Value should be equal or greater than 1'),
            MaxValueValidator(limit_value=66, message='Value should be equal or less than 66')
        ],
        error_messages={
            'blank': 'This field cannot be blank',
            'unique': 'You have already entered data for this period'
        }
    )
    method = models.CharField(
        max_length=15,
        choices=SNAMethod.choices,
        error_messages={
            'blank': 'This field cannot be blank'
        }
    )

    class Meta:
        constraints= [
            models.UniqueConstraint(fields=['user', 'period'], name='users_period')
        ]
