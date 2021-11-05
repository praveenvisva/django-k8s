from django.urls import path
from . import views

app_name = "students"
urlpatterns = [
    # Students List View
    path('', views.ListView.as_view(), name='list'),
    path("<int:pk>/", views.DetailView.as_view(), name='detail')]
