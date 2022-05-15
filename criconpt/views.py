from django.shortcuts import render

# Create your views here.

def ptform(request):
    return render(request, 'criconpt/ptform.html', {})

