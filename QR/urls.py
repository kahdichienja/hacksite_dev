from django.urls import path
from . import views
appname = 'QR'
urlpatterns = [
    path('', views.hacker_view, name = 'hacker'),
    path('hack/', views.myview, name = 'hackqr'),
]