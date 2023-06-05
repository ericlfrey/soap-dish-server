from django.db import models


class Favorite(models.Model):

    user = models.ForeignKey(
        "Soaper", on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        "Recipe", on_delete=models.CASCADE)
