from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
	path('polls/',include('polls.urls')),
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls'))
]
