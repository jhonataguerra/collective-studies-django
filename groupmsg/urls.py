from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

]

# app base
urlpatterns += [
    path('', include('base.urls')),
]

# api base
urlpatterns += [
    path('api/', include('base.api.urls')),
]