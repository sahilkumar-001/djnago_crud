
from django.contrib import admin
from django.urls import path,include
from new_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('new_app.urls')),
    
    
]
