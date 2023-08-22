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


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class CurrentWeather(BaseModel):
    dt: int
    sunrise: int
    sunset: int
    temp: float
    feels_like: float
    pressure: int
    humidity: int
    dew_point: float
    uvi: float
    clouds: int
    visibility: int
    wind_speed: float
    wind_deg: int
    wind_gust: float
    weather: list[Weather]


class MinutelyWeather(BaseModel):
    dt: int
    precipitation: int


class HourlyWeather(BaseModel):
    dt: int
    temp: float
    feels_like: float
    pressure: int
    humidity: int
    dew_point: float
    uvi: int
    clouds: int
    visibility: int
    wind_speed: float
    wind_deg: int
    wind_gust: float
    weather: list[Weather]
    pop: float


class DailyWeather(BaseModel):
    class Temperature(BaseModel):
        day: float
        min: float
        max: float
        night: float
        eve: float
        morn: float

    class FeelsLike(BaseModel):
        day: float
        night: float
        eve: float
        morn: float

    dt: int
    sunrise: int
    sunset: int
    moonrise: int
    moonset: int
    moon_phase: float
    summary: str
    temp: Temperature
    feels_like: FeelsLike
    pressure: int
    humidity: int
    dew_point: float
    wind_speed: float
    wind_deg: int
    wind_gust: float
    weather: list[Weather]
    clouds: int
    pop: float
    rain: float
    uvi: float


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
