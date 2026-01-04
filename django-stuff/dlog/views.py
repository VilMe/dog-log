from django.http import HttpResponse

from .models import FoodAmount

def index(request):
    latest_food_amounts_list = FoodAmount.objects.order_by("-feed_date")[:5]
    output = ", ".join([f.cups_of_kibble for f in latest_food_amounts_list])
    return HttpResponse(output)


def detail(request):
    return HttpResponse("You're looking at dog log form")


def results(request):
    return HttpResponse("You're looking at dog log results table ")

