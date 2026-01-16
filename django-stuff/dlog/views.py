from django.http import HttpResponse
from django.template import loader

from .models import FoodAmount

def index(request):
    latest_food_amounts_list = FoodAmount.objects.order_by("-feed_date")[:5]
    template = loader.get_template("dlog/index.html")
    context = {"latest_food_amounts_list": latest_food_amounts_list}
    return HttpResponse(template.render(context, request))


def form(request):
    template = loader.get_template("dlog/form.html")
    return HttpResponse(template.render())


def record(request):

    return HttpResponse("You're looking at dog log record function")

