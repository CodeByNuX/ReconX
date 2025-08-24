import json
from django.shortcuts import render
from services.rapidapi import is_domain, is_ipv4, whois_lookup, ip_risk_lookup

# Create your views here.
def home(request):
    result = None
    error = None

    if request.method == 'POST':
        
        
        query = (request.POST.get('query') or '').strip()
        
        if not query:
            error = (                
                'You need to pass a valid domain or IPv4 address.\n\n'
                'Examples:\n www.xyz.com\n 1.2.3.4\n'
            )
        else:
            
            try:
                
                if is_domain(query):                                  

                    data = whois_lookup(query)

                elif is_ipv4(query):                    
                    
                    whois_data = whois_lookup(query)
                    ip_risk_data = ip_risk_lookup(query)
                    

                    data = {'whois':whois_data,'ip_risk':ip_risk_data}
                    


                else:
                    data = None
                    error = (
                        'You need to pass a valid domain or IPv4 address.\n\n'
                        'Examples:\n www.xyz.com\n 1.2.3.4\n'
                    )
                
                if data is not None:
                    if isinstance(data, (dict,list)):
                        result = json.dumps(data,indent=2,sort_keys=True)
                    else:
                        result = str(data)

            except Exception as e:
                error = f'{e}'        

    return render(request, 'reconx/home.html', {'result': result, 'error': error})