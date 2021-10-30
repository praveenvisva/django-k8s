from django.urls import path
from . import views

app_name = "students"
urlpatterns = [
    # Students List View
    path('', views.list, name='list'),
    path("<int:id>/", views.detail, name='detail')]
