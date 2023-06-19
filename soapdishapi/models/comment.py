from django.db import models


class Comment(models.Model):

    soaper = models.ForeignKey(
        "Soaper", on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
