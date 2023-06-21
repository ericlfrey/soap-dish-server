from django.db import models
from .soaper import Soaper
from .recipe import Recipe


class Comment(models.Model):

    soaper = models.ForeignKey(Soaper, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    # custom property to get the soaper name for serializer
    @property
    def commenter_name(self):
        '''Custom Property to get the soaper name'''
        return f'{self.soaper.first_name} {self.soaper.last_name}'
