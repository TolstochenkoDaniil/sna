from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from registration.views import RegistrationView
from user_stats.views import UserStatisticView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='/'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', RegistrationView.as_view(), name='registration'),
    path('statistic/', UserStatisticView.as_view(), name='statistic')
]
