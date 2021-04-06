
import pandas as pd
import plotly.express as px
import plotly.offline as opy
from typing import Any, Dict, Type

from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.db.models import F

from user_stats.forms import UserStatisticForm
from user_stats.models import UserStats


class UserStatisticView(FormView):
    template_name = 'statistic/user.html'
    form_class = UserStatisticForm

    def get_initial(self):
        return {'user': self.request.user.id}

    def form_valid(self, form: Type[UserStatisticForm]) -> HttpResponse:
        form = form.save(commit=False)
        form.user_id = self.request.user.id
        form.save()

        return super().form_valid(form)

    def get_success_url(self) -> str:
        return self.request.path


class UserStatsPlotView(TemplateView):
    ''''''
    template_name = 'statistic/visualization.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        columns = [col.name for col in UserStats._meta.fields]
        data = pd.DataFrame.from_records(
            UserStats.objects.annotate(week=F('period') % 7).filter(week=0).values_list(*columns),
            columns=columns
        )
        figure = px.box(data, x='period', y='activity', color='method')
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['user_stats'] = div

        return context
