from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from registration.views import RegistrationView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='/'),
    # path('', TemplateView.as_view(template_name='methods/description.html'), name='/methods'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', RegistrationView.as_view(), name='registration')
]
