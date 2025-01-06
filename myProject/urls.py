from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin site
    path('', include('WebBuilder.urls')),  # Include URLs from your app
]
