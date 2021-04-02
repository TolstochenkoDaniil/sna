
from typing import Any, Dict, Type
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from user_stats.forms import UserStatisticForm


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

        div = None
        context['user_stats'] = div
        
        return context
