from django.contrib import admin
from django.urls import path
from naty_agendamento import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.CreateAccountView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('schedule/', views.CreateScheduleView.as_view()),
]
