from django.shortcuts import render

def sentiment(request):
    return render(request, 'sentiment/index.html', {"sentiment_url":"http://localhost:8501"})
