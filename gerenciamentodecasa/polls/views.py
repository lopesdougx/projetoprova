from django.http import HttpResponse


def index(request):
    return HttpResponse("Rafael é o melhor")