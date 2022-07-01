from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('send_email/', views.send_email, name="index"),
    path('send_email/home/', views.index, name="index")
]