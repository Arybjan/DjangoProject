from django.db import models


# Create your models here.
class Dish(models.Model):
    title = models.CharField(max_length=100)
    sizes = models.ManyToManyField("SizeType", through="dishes.DishSize")


class SizeType(models.Model):
    name = models.CharField(max_length=100)


class DishSize(models.Model):
    dish = models.ForeignKey("dishes.Dish", on_delete=models.CASCADE)
    size_type = models.ForeignKey(
        "dishes.SizeType", on_delete=models.CASCADE
    )
    size_value = models.FloatField()
    weight = models.FloatField()
    price = models.PositiveIntegerField()
