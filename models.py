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
    precipitation: float


class HourlyWeather(BaseModel):
    dt: int
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


class Alert(BaseModel):
    sender_name: str
    event: str
    start: int
    end: int
    description: str
    tags: list[str]


class WeatherAnalytics(BaseModel):
    pass


class WeatherForecast(BaseModel):
    lat: float
    lon: float
    timezone: str
    timezone_offset: int
    current: CurrentWeather
    minutely: list[MinutelyWeather]
    hourly: list[HourlyWeather]
    daily: list[DailyWeather]
    alerts: list[Alert]


class WeatherUpdate(BaseModel):
    lat: float
    lon: float
    timezone: str
    timezone_offset: int
    current: dict
    alerts: list[Alert]
