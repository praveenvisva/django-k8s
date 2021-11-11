from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from students.models import Student
from students.serializers import StudentSerializer


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = "id"
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class StudentAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetails(APIView):
    def get_object(self, id):
        try:
            student = Student.objects.get(id=id)
            return student
        except Student.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        student = self.get_object(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = self.get_object(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = self.get_object(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.

# def list(request):
#     students = Student.objects.all()
#     result = []
#     for student in students:
#         result.append({"id": student.id,
#                        "name": student.first_name})
#     context = {"result": result}
#     # template = loader.get_template("students/list.html")
#     #
#     # return HttpResponse(template.render(context, request))
#     return render(request, "students/list.html", context)
#
#
# def detail(request, id):
#     # try:
#     #     student = Student.objects.filter(pk=id)
#     # except Student.DoesNotExist:
#     #     raise Http404("Student Does Not Exist!")
#     student = get_object_or_404(Student, id=id)
#     return render(request, "students/detail.html", {"student": student})

# class DetailView(generic.DetailView):
#     model=Student
#     template_name = "students/detail.html"
#
#
# class ListView(generic.ListView):
#     template_name = "students/list.html"
#     context_object_name = 'result'
#     paginate_by = 5
#     def get_queryset(self):
#         return Student.objects.all()
#
# class DeleteView(generic.DeleteView):
#     template_name = "students/delete.html"
#     context_object_name = 'student'
#     def delete(self, request, *args, **kwargs):
#         return Student.objects.all()
#
# class CreateView(generic.CreateView):
#     template_name = "students/create.html"
#     context_object_name = 'student'

# @api_view(['GET'])
# def student_collection(request):
#     if request.method == "GET":
#         studs = Student().objects.all()
#         serializer = StudentSerializer(studs,many=True)
#         return Response(serializer.data)
#
# @api_view(['GET'])
# def student_detail(request,pk):
#     try:
#         stud = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == "GET":
#         serializer = StudentSerializer(stud)
#         return Response(serializer.data)
@api_view(["GET", "POST"])
def student_list(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
