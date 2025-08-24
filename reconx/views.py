import json
from django.shortcuts import render
from services.rapidapi import lookup

# Create your views here.
def home(request):
    result = None
    error = None

    if request.method == 'POST':
        query = (request.POST.get('query') or '').strip()
        try:
            data = lookup(query)
            
            if isinstance(data, (dict,list)):
                # pretty print / indent
                result = json.dumps(data,indent=2,sort_keys=True)
            else:
                result = str(data)
            
            
        except Exception as e:
            error = f"{e}"

    return render(request, 'reconx/home.html', {'result': result, 'error': error})