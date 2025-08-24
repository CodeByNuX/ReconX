import json
import os
import re
import ipaddress
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# --- Config from environment ---
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
WHOIS_API_HOST = os.getenv('WHOIS_API_HOST', 'whois40.p.rapidapi.com')
IP_RISK_API_HOST = os.getenv('IP_RISK_API_HOST', 'ip-geolocation-and-threat-detection.p.rapidapi.com')



def is_domain(query:str)->bool:
    _domain_regex = re.compile('^(?!-)([A-Za-z0-9-]{1,63}\.)+[A-Za-z]{2,63}$')
    return bool(_domain_regex.match(query))

def is_ipv4(query:str)->bool:
    try:
        ipaddress.ip_address(query)
        return True
    except ValueError:
        return False

def whois_lookup(query:str):

    url = f'https://{WHOIS_API_HOST}/whois'
    querystring = {'q': query}
    
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': WHOIS_API_HOST,
        'accept': 'application/json',
    }

    response = requests.get(url,headers=headers, params=querystring,timeout=(10,15))
    response.raise_for_status()
    return response.json()

def ip_risk_lookup(query):
    url = f'https://{IP_RISK_API_HOST}/v1/ipsight/{query}'
 

