from django.db import models
from .recipe_oil import RecipeOil
from .soaper import Soaper
from .favorite import Favorite


class Recipe(models.Model):

    maker = models.ForeignKey(
        "Soaper", on_delete=models.CASCADE, related_name='organized_events')
    title = models.CharField(max_length=50)
    water_amount = models.DecimalField(max_digits=5, decimal_places=3)
    lye_amount = models.DecimalField(max_digits=5, decimal_places=3)
    super_fat = models.DecimalField(max_digits=5, decimal_places=3)
    description = models.CharField(max_length=500, blank=True)
    notes = models.CharField(max_length=500, blank=True)
    public = models.BooleanField(default=False)
    oils = models.ManyToManyField(
        'Oil', related_name="oils", through=RecipeOil)
    comments = models.ManyToManyField(
        'Comment', related_name="comments", through='RecipeComment')
    favorites = models.ManyToManyField(
        Soaper, through=Favorite, related_name='favorites')

    @property
    def favorite(self):
        """Custom Property"""
        return self.__favorite

    @favorite.setter
    def favorite(self, value):
        self.__favorite = value
