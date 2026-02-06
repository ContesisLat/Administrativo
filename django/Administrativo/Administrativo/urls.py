from django.contrib import admin
from django.urls import path, include
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('desarrollo.urls')),
    path('api3/', include('contabilidad.urls'))
]
 
