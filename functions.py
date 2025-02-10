from math import radians, sin, cos, sqrt, atan2
import requests

def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    R = 6371
    return R * c

def geocode_city(name: str) -> dict:
    headers = {"User-Agent": "CityAPI/1.0"}
    url = f"https://nominatim.openstreetmap.org/search?q={name}&format=json"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data:
                return {
                    "latitude": float(data[0]["lat"]),
                    "longitude": float(data[0]["lon"]),
                }
        return None
    except requests.exceptions.RequestException:
        return None