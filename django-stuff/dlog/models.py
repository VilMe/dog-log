from django.db import models

# How many cups of kibble I fed goose
class FoodAmount(models.Model):
    feed_date = models.DateField()
    cups_of_kibble = models.DecimalField(max_digits=4, decimal_places=1)

    # return a string for the record of cups of kibble fed
    def __str__(self):
        return f'{self.feed_date} {self.cups_of_kibble} cups'

# Notes and observations

class Observation(models.Model):
    note_weight_date = models.ForeignKey(FoodAmount, on_delete=models.CASCADE)
    weight = models.IntegerField()
    note = models.TextField()

    # returns weight and notes
    def __str__(self):
        return f'{self.weight} lbs and/or notes for this day: {self.note}'