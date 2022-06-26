from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('send_email/', views.send_email, name="index"),
    path('send_email/home/', views.index, name="index")
]