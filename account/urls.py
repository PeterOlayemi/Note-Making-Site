from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('register/', views.register.as_view(), name='register'),
    path('password_reset/', views.password_reset_request, name="password_reset")
]
