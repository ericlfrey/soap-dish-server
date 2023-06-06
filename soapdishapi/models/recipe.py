from django.db import models
from .oil import Oil
from .recipe_oil import RecipeOil


class Recipe(models.Model):

    maker = models.ForeignKey(
        "Soaper", on_delete=models.CASCADE, related_name='organized_events')
    title = models.CharField(max_length=50)
    water_amount = models.DecimalField(max_digits=5, decimal_places=3)
    lye_amount = models.DecimalField(max_digits=5, decimal_places=3)
    super_fat = models.DecimalField(max_digits=5, decimal_places=3)
    description = models.CharField(max_length=100)
    notes = models.CharField(max_length=200)
    public = models.BooleanField(default=False)
    oils = models.ManyToManyField(Oil, related_name="oils", through=RecipeOil)
