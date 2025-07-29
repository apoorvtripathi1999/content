from django.db import models

class sentiment(models.Model):
    
    overall = models.IntegerField(max_length=1)
    verified = models.BooleanField()
    reviewTime = models.DateField()
    reviewerID = models.CharField(max_length=100)
    asin = models.CharField(max_length=100)
    style = models.JSONField(null=True, blank=True)
    reviewrName = models.CharField(max_length=50)
    reviewText = models.CharField(max_length=500)
    reviewSummary = models.CharField(max_length=250)
    unixTime = models.IntegerField(max_length=50)
    vote = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
