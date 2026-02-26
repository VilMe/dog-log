from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import FoodAmount,Observation

def index(request):
    latest_food_amounts_list = FoodAmount.objects.order_by("-feed_date")[:5]
    # get observations, notes and weight
    if latest_food_amounts_list.observation_set.exists():
        observations = latest_food_amounts_list.observation_set.all()

    template = loader.get_template("dlog/index.html")
    context = {"latest_food_amounts_list": latest_food_amounts_list}
    return HttpResponse(template.render(context, request))


def form(request):
    # template = loader.get_template("dlog/form.html")
    return render(request, "dlog/form.html")


def record(request):
    feed_date = request.POST['feed_date']
    # print("*" * 10)
    # print(feed_date)
    # print("*" * 10)
    cups_of_kibble = request.POST.get('cups_of_kibble')
    feed_info = FoodAmount(
        feed_date=feed_date, 
        cups_of_kibble=cups_of_kibble
    )
    weight = request.POST.get('weight')
    note = request.POST.get('note')
    feed_info.save()
    feed_info.observation_set.create(
        weight=weight,
        note=note
    )

    
    return HttpResponseRedirect("/dlog/")

