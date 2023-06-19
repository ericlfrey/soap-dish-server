from django.db import models


class RecipeComment(models.Model):

    recipe = models.ForeignKey(
        "Recipe", on_delete=models.CASCADE, related_name='recipe_comments')
    comment = models.ForeignKey(
        "Comment", on_delete=models.CASCADE)
