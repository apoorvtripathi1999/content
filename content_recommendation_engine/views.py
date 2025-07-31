from django.shortcuts import render

def home(request):
    
    return render(request, 'sentiment/index.html', {"sentiment_url":"http://localhost:8501"})
