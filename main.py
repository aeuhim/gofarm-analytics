import json
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse

from models import (
    Address,
    Geolocation,
    WeatherAnalytics,
    WeatherForecast,
    WeatherUpdate,
)
from utils import (
    analyze_local_weather,
    fetch_geolocation_weather,
    host_to_geolocation,
    geolocation_to_address,
)

with open("manifest.json") as file:
    manifest = json.load(file)
    title = manifest["name"]
    summary = manifest["description"]
    version = manifest["version"]
    contact = {
        "email": manifest["author"]["email"],
        "url": manifest["url"],
    }
    license_info = {
        "name": manifest["license"]["name"],
        "url": manifest["license"]["url"],
    }

app = FastAPI(
    title=title,
    summary=summary,
    version=version,
    contact=contact,
    license_info=license_info,
)


@app.get("/", response_class=RedirectResponse)
def receive_documentation() -> RedirectResponse:
    url = "/redoc"

    return RedirectResponse(url)


@app.get("/geolocation2address", response_class=JSONResponse)
def receive_address_from_geolocation(
    request: Request, latitude: float = None, longitude: float = None
) -> Address:
    if not latitude or not longitude:
        geolocation = host_to_geolocation(request.client.host)
    else:
        geolocation = {"latitude": latitude, "longitude": longitude}

    if "error" in geolocation and geolocation["error"]:
        return JSONResponse(geolocation)

    address = geolocation_to_address(geolocation["latitude"], geolocation["longitude"])

    return JSONResponse(address)


@app.get("/host2geolocation", response_class=JSONResponse)
def receive_geolocation_from_host(request: Request, host: str = None) -> Geolocation:
    if not host:
        geolocation = host_to_geolocation(request.client.host)
    else:
        geolocation = host_to_geolocation(host)

    return JSONResponse(geolocation)


@app.get("/weather", response_class=JSONResponse)
def receive_weather_update(
    request: Request, latitude: float = None, longitude: float = None
) -> WeatherUpdate:
    if not latitude or not longitude:
        geolocation = host_to_geolocation(request.client.host)
    else:
        geolocation = {"latitude": latitude, "longitude": longitude}

    if "error" in geolocation and geolocation["error"]:
        return JSONResponse(geolocation)

    weather = fetch_geolocation_weather(
        geolocation["latitude"], geolocation["longitude"], "minutely,hourly,daily"
    )

    return JSONResponse(weather)


@app.get("/weather/analytics")
def receive_weather_analytics(
    request: Request, latitude: float = None, longitude: float = None
) -> WeatherAnalytics:
    if not latitude or not longitude:
        geolocation = host_to_geolocation(request.client.host)
    else:
        geolocation = {"latitude": latitude, "longitude": longitude}

    if "error" in geolocation and geolocation["error"]:
        return JSONResponse(geolocation)

    address = geolocation_to_address(geolocation["latitude"], geolocation["longitude"])

    if "error" in address and address["error"]:
        return JSONResponse(address)

    weather = fetch_geolocation_weather(
        geolocation["latitude"], geolocation["longitude"], "minutely"
    )

    if "error" in weather and weather["error"]:
        return JSONResponse(weather)

    data = {**address, **weather}

    result = analyze_local_weather(data)

    return JSONResponse(result)


@app.get("/weather/forecast")
def receive_weather_forecast(
    request: Request, latitude: float = None, longitude: float = None, exclude: str = ""
) -> WeatherForecast:
    if not latitude or not longitude:
        geolocation = host_to_geolocation(request.client.host)
    else:
        geolocation = {"latitude": latitude, "longitude": longitude}

    if "error" in geolocation and geolocation["error"]:
        return JSONResponse(geolocation)

    weather = fetch_geolocation_weather(
        geolocation["latitude"], geolocation["longitude"], exclude
    )

    return JSONResponse(weather)
