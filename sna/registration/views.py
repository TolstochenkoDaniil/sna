from typing import Type
from django.http.response import HttpResponse
from django.views.generic.edit import FormView

from registration.forms import RegistrationForm


class RegistrationView(FormView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form: Type[RegistrationForm]) -> HttpResponse:
        form.save()

        return super().form_valid(form)