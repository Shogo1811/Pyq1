from django.contrib import admin
from django.urls import path, include # includeを追加

urlpatterns = [
    path('garden/', include('garden.urls')),
    path('admin/', admin.site.urls),
]
