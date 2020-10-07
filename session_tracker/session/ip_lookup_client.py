import json
import requests
from django.conf import settings

base_url = settings.RAPIDAPI_URL

headers = {
    'x-rapidapi-host': settings.RAPIDAPI_HOST,
    'x-rapidapi-key': settings.RAPIDAPI_KEY,
    'accept': "application/json"
}


def get_ip_details(ip):
    url = base_url + ip
    response = requests.request("GET", url, headers=headers)
    ip_info = json.loads(response.content)
    return ip_info
