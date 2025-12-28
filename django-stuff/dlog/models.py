from django.db import models

# How many cups of kibble I fed goose
class FoodAmount(models.Model):
    feed_date = models.DateField()
    cups_of_kibble = models.DecimalField(max_digits=4, decimal_places=1)

# Notes and observations

class Observation(models.Model):
    weight = models.IntegerField()
    note = models.TextField()