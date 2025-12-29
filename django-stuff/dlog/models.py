from django.db import models

# How many cups of kibble I fed goose
class FoodAmount(models.Model):
    feed_date = models.DateField()
    cups_of_kibble = models.DecimalField(max_digits=4, decimal_places=1)


    def __str__(self):
        return self.feed_date, self.cups_of_kibble

# Notes and observations

class Observation(models.Model):
    note_weight_date = models.ForeignKey(FoodAmount, on_delete=models.CASCADE)
    weight = models.IntegerField()
    note = models.TextField()


    def __str__(self):
        return self.weight, self.note