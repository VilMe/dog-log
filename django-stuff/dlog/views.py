from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at my dog log index. WOOOOOOT! need to add mysql db next!!!!!")