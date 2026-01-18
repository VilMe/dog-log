from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import FoodAmount,Observation

def index(request):
    latest_food_amounts_list = FoodAmount.objects.order_by("-feed_date")[:5]
    template = loader.get_template("dlog/index.html")
    context = {"latest_food_amounts_list": latest_food_amounts_list}
    return HttpResponse(template.render(context, request))


def form(request):
    template = loader.get_template("dlog/form.html")
    return HttpResponse(template.render())


def record(request):
    if request.method == "POST":
        feed_date = request.POST.get('feed_date')
        cups_of_kibble = request.POST.get('cups_of_kibble')
        feed_info = FoodAmount(feed_date=feed_date, cups_of_kibble=cups_of_kibble)
        feed_info.save
    return render(request, "You're looking at dog log record function")

