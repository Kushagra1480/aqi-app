import requests
from django.core.management.base import BaseCommand
from backend.models import AirQuality, Location

class Command(BaseCommand):
    def handle(self, *args, **options):
        api_key = "4a23e08c-2df6-45da-90a6-c7d53e49be0b"
        url = f"http://api.airvisual.com/v2/city?city=Los%Angeles&state=California&country=USA&key={api_key}"
        
        response = requests.get(url)
        data = response.json()
        
        try:
            location = Location.objects.get(name="Paris") 
        except Location.DoesNotExist:
            location = Location.objects.create(name="Paris", coordinates="...")
        
        AirQuality.objects.create(
            location = location, 
            aqi = data['data']['current']['pollution']['aqius'],
            time = data['data']['current']['weather']['ts']
        )