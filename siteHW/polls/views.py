from django.shortcuts import render
from django.http import HttpResponse
from FuncForDB import sel

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



def index(request):
    a = sel()
    return render(request, 'polls/index.html', {'data': a})

# def index(request):
#     return render(request, 'polls/index.html')
