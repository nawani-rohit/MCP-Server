import requests
from fastapi import HTTPException

SPACEX_URL = "https://api.spacexdata.com/v3/launches"

def fetch_launches():
    try:
        resp = requests.get(SPACEX_URL)
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Network error: {e}")
    if resp.status_code != 200:
        raise HTTPException(status_code=502, detail="SpaceX API error")
    
    try:
        return resp.json()
    except ValueError:
        raise HTTPException(status_code=502, detail="Invalid JSON data from API")