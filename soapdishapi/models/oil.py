from django.db import models
from .recipe import Recipe
from .recipe_oil import RecipeOil


class Oil(models.Model):

    name = models.CharField(max_length=50)
    sap = models.DecimalField(max_digits=5, decimal_places=3)
    recipes = models.ManyToManyField(Recipe, through=RecipeOil)
