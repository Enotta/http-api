from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import requests
from typing import List
from math import radians, sin, cos, sqrt, atan2

import models
import schemas
from functions import geocode_city, haversine
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/cities/", response_model=schemas.City)
def create_city(city: schemas.CityCreate, db: Session = Depends(get_db)):
    existing_city = db.query(models.City).filter(models.City.name == city.name).first()
    if existing_city:
        raise HTTPException(status_code=400, detail="City already exists")
    
    coords = geocode_city(city.name)
    if not coords:
        raise HTTPException(status_code=404, detail="City coordinates not found")
    
    db_city = models.City(
        name=city.name,
        latitude=coords["latitude"],
        longitude=coords["longitude"]
    )
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


@app.get("/cities/", response_model=List[schemas.City])
def read_cities(db: Session = Depends(get_db)):
    cities = db.query(models.City).all()
    return cities


@app.delete("/cities/{city_id}")
def delete_city(city_id: int, db: Session = Depends(get_db)):
    db_city = db.query(models.City).filter(models.City.id == city_id).first()
    if not db_city:
        raise HTTPException(status_code=404, detail="City not found")
    db.delete(db_city)
    db.commit()
    return {"message": "City deleted successfully"}


@app.get("/cities/nearby", response_model=List[schemas.City])
def get_nearby_cities(lat: float, lon: float, db: Session = Depends(get_db)):
    cities = db.query(models.City).all()
    if not cities:
        return []
    
    cities_with_dist = [
        (city, haversine(lon, lat, city.longitude, city.latitude))
        for city in cities
    ]
    sorted_cities = sorted(cities_with_dist, key=lambda x: x[1])
    
    return [city[0] for city in sorted_cities[:2]]
    