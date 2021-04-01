from django.forms import ModelForm
from user_stats.models import UserStats


class UserStatisticForm(ModelForm):
    ''''''
    class Meta:
        model = UserStats
        fields = ('activity', 'period', 'method')
        exclude = ('user_id',)