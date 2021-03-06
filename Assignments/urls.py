from django.contrib import admin
from django.urls import path, include

from dashboard.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('dashboard/', include('dashboard.urls')),
    path('auth/', include('accounts.urls')),
    path('assignments/', include('assignment.urls')),
]
