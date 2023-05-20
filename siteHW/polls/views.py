from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    a = "<table border = '5'><tr><td>meow</td></tr></table>"
    return render(request, 'polls/category.html', {'data': a})
