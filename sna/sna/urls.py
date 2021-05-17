from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from registration.views import RegistrationView
from user_stats.views import UserStatisticView, UserStatsPlotView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='/'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', RegistrationView.as_view(), name='registration'),
    path('statistic/', UserStatisticView.as_view(), name='statistic'),
    path('statistic/charts', UserStatsPlotView.as_view(), name='charts')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
