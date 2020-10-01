from django.urls import path

from backend.Api.v1 import views

urlpatterns = [
    path('api/login/', views.LoginView.as_view(), name = 'login_view')
]