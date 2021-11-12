from django.urls import path,include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import student_list,student_detail,StudentAPIView,StudentDetails,GenericAPIView,StudentViewSet
router = DefaultRouter()
router.register('student',StudentViewSet,basename='student')
app_name = "students"
urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>',include(router.urls)),
    # Students List View
    # path('', views.ListView.as_view(), name='list'),
    # path("<int:pk>/", views.DetailView.as_view(), name='detail')
    #path('students/',student_list),
    path('student/',StudentAPIView.as_view()),
    #path('detail/<int:pk>',student_detail)
    path('detail/<int:id>',StudentDetails.as_view()),
path('generic/student/<int:id>',GenericAPIView.as_view()),
]
