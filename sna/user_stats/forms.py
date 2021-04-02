from django.forms import ModelForm, HiddenInput
from user_stats.models import UserStats


class UserStatisticForm(ModelForm):
    ''''''
    class Meta:
        model = UserStats
        fields = ('activity', 'period', 'method', 'user')
        widgets = {
            'user': HiddenInput,
        }