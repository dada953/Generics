from django.urls import path
from home.views import RegisterView
urlpatterns = [
    
    path('register/', RegisterView.as_view(), name='register'),]