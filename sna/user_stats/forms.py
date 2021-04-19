from django.forms import ModelForm, HiddenInput, NumberInput
from user_stats.models import UserStats


class UserStatisticForm(ModelForm):
    ''''''
    class Meta:
        model = UserStats
        fields = ('activity', 'period', 'method', 'user')
        widgets = {
            'user': HiddenInput,
            'activity': NumberInput(
                attrs={
                    'placeholder':'Enter time in hours'
                }),
            'period': NumberInput(
                attrs={
                    'placeholder':'Enter day number'
                })
        }