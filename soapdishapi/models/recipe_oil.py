from django.db import models


class RecipeOil(models.Model):

    recipe = models.ForeignKey(
        "Recipe", on_delete=models.CASCADE, related_name='recipe_oils')
    oil = models.ForeignKey(
        "Oil", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=3)
