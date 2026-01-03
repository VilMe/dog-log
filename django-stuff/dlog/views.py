from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at my dog log index. WOOOOOOT! need to add mysql db next!!!!!")


def detail(request):
    return HttpResponse("You're looking at dog log form")


def results(request):
    return HttpResponse("You're looking at dog log results table ")

