
from typing import Type
from django.http.response import HttpResponse
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
