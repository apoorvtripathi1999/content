from django.urls import path
from .views import sentiment

urlpatterns = [
    path('', sentiment, name='sentiment_url'),
]