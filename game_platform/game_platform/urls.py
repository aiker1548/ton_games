from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rooms.urls')),
    path('api/', include('games.urls')),    
    path('api/users/', include('users.urls'))
]
