from django.db import models

class MywatchlistItem(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    rating = models.IntegerField()
    review = models.TextField()
    watched = models.CharField(max_length=255)