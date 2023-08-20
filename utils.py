import os, requests
from dotenv import load_dotenv

load_dotenv()


def analyze_local_weather(data: dict) -> dict:
    return {}


def fetch_geolocation_weather(latitude: float, longitude: float, exclude: str) -> dict:
    try:
        domain = "https://api.openweathermap.org/data/3.0/onecall"
        openweather_api_key = os.getenv("OPENWEATHER_API_KEY")
        url = f"{domain}?lat={latitude}&lon={longitude}&exclude={exclude}&appid={openweather_api_key}"
        response = requests.get(url)

    except Exception as e:
        return {
            "error": True,
            "reason": type(e).__name__,
        }

    if response.status_code != 200:
        return {
            "error": True,
            "reason": response.reason,
        }

    json_response = response.json()

    return json_response


def geolocation_to_address(latitude: float, longitude: float) -> dict:
    try:
        domain = "https://dev.virtualearth.net/REST/v1/Locations"
        include = "ciso2"
        is_verbose_names = True
        bingmaps_api_key = os.getenv("BINGMAPS_API_KEY")
        url = f"{domain}/{latitude},{longitude}?incl={include}&vbpn={is_verbose_names}&key={bingmaps_api_key}"
        response = requests.get(url)

    except Exception as e:
        return {
            "error": True,
            "reason": type(e).__name__,
        }

    if response.status_code != 200:
        return {
            "error": True,
            "reason": response.reason,
        }

    json_response = response.json()

    if json_response["resourceSets"][0]["estimatedTotal"] == 0:
        return {
            "error": True,
            "reason": "No Resource Found",
        }

    resource = json_response["resourceSets"][0]["resources"][0]

    if (
        "address" not in resource
        or "locality" not in resource["address"]
        or "adminDistrict" not in resource["address"]
        or "countryRegion" not in resource["address"]
        or "postalCode" not in resource["address"]
        or "countryRegionIso2" not in resource["address"]
    ):
        return {"error": True, "reason": "Reverse Geocoding Failed"}

    return {
        "locality": resource["address"]["locality"],
        "district": resource["address"]["adminDistrict"],
        "country": resource["address"]["countryRegion"],
        "postal": resource["address"]["postalCode"],
        "iso": resource["address"]["countryRegionIso2"],
    }


def host_to_geolocation(host: str) -> dict:
    try:
        domain = "https://ipapi.co"
        url = f"{domain}/{host}/json"
        response = requests.get(url)

    except Exception as e:
        return {
            "error": True,
            "reason": type(e).__name__,
        }

    if response.status_code != 200:
        return {
            "error": True,
            "reason": response.reason,
        }

    json_response = response.json()

    if "error" in json_response and json_response["error"]:
        return {
            "error": json_response["error"],
            "reason": json_response["reason"],
        }

    return {
        "latitude": json_response["latitude"],
        "longitude": json_response["longitude"],
    }
