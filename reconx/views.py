from django.shortcuts import render
from services.rapidapi import lookup

# Create your views here.
def home(request):
    result = None
    error = None

    if request.method == 'POST':
        query = (request.POST.get('query') or '').strip()
        try:
            result = lookup(query)
            
        except Exception as e:
            error = f"{e}"

    return render(request, 'reconx/home.html', {'result': result, 'error': error})