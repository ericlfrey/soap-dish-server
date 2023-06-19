from django.db import models
from .comment import Comment
from .recipe import Recipe


class RecipeComment(models.Model):

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='recipe_comments')
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE)

    # custom property to get the comment text for serializer
    @property
    def comment_text(self):
        '''Custom Property to get the comment text'''
        return f'{self.comment.text}'

    # custom property to get the soaper name for serializer
    @property
    def commenter(self):
        '''Custom Property to get the soaper name'''
        return f'{self.recipe.maker.first_name} {self.recipe.maker.last_name}'
