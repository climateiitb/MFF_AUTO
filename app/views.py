import time
from .utils import MCGM_data
from .models import WeatherData

def fetch_and_store_data():
    while True:
        data = MCGM_data()
        if data:
            WeatherData.objects.create(**data)
            print("Data stored successfully.")
        else:
            print("Failed to fetch data.")
        time.sleep(9)
        
fetch_and_store_data()

print("aa")