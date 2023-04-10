from django.http import HttpResponse


def index_view():
    return HttpResponse('hello world')
