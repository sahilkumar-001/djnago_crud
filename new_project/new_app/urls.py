
from django.contrib import admin
from django.urls import path
from new_app import views
from .views import RegisterUser
from .views import LoginView , LogoutView
# from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('register', views.RegisterUser.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),

    # path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]
