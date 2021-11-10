from django.urls import path
from django.conf.urls import url
from .views import student_list,student_detail
app_name = "students"
urlpatterns = [
    # Students List View
    # path('', views.ListView.as_view(), name='list'),
    # path("<int:pk>/", views.DetailView.as_view(), name='detail')
    path('students/',student_list),
    path('detail/<int:pk>',student_detail)
]
