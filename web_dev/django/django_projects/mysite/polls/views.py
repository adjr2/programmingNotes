from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, you are the poll index.")