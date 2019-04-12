from django.db import models


class Articles(models.Model):

    title = models.CharField(max_length=120)
    post = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images', blank=True)


def __str__(self):
    return self.title
