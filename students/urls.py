from django.urls import path
from django.conf.urls import url
from .views import student_list,student_detail,StudentAPIView,StudentDetails,GenericAPIView
app_name = "students"
urlpatterns = [
    # Students List View
    # path('', views.ListView.as_view(), name='list'),
    # path("<int:pk>/", views.DetailView.as_view(), name='detail')
    #path('students/',student_list),
    path('student/',StudentAPIView.as_view()),
    #path('detail/<int:pk>',student_detail)
    path('detail/<int:id>',StudentDetails.as_view()),
path('generic/student/<int:id>',GenericAPIView.as_view()),
]
