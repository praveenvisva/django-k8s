from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Student
from django.http import Http404


# Create your views here.

def list(request):
    students = Student.objects.all()
    result = []
    for student in students:
        result.append({"id": student.id,
                       "name": student.first_name})
    context = {"result": result}
    # template = loader.get_template("students/list.html")
    #
    # return HttpResponse(template.render(context, request))
    return render(request, "students/list.html", context)


def detail(request, id):
    # try:
    #     student = Student.objects.filter(pk=id)
    # except Student.DoesNotExist:
    #     raise Http404("Student Does Not Exist!")
    student = get_object_or_404(Student, id=id)
    return render(request, "students/detail.html", {"student": student})
