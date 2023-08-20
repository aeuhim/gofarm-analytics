from pydantic import BaseModel


class Address(BaseModel):
    locality: str
    district: str
    country: str
    postal: str
    iso: str


class Geolocation(BaseModel):
    latitude: float
    longitude: float


class WeatherAnalytics(BaseModel):
    pass


class WeatherForecast(BaseModel):
    lat: float
    lon: float
    timezone: str
    timezone_offset: str
    current: dict
    minutely: list[dict]
    hourly: list[dict]
    daily: list[dict]
    alerts: list[dict]


class WeatherUpdate(BaseModel):
    lat: float
    lon: float
    timezone: str
    timezone_offset: str
    current: dict
    alerts: list[dict]
