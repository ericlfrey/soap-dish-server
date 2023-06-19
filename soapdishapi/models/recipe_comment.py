from django.db import models
from .comment import Comment
from .recipe import Recipe


class RecipeComment(models.Model):

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='recipe_comments')
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE)

    # custom property to get the soaper name for serializer
    @property
    def commenter(self):
        '''Custom Property to get the soaper name'''
        return f'{self.comment.soaper.first_name} {self.comment.soaper.last_name}'

    # custom property to get the comment text for serializer
    @property
    def comment_id(self):
        '''Custom Property to get the comment id'''
        return f'{self.comment.id}'
    # custom property to get the comment text for serializer

    @property
    def text(self):
        '''Custom Property to get the comment text'''
        return f'{self.comment.text}'
