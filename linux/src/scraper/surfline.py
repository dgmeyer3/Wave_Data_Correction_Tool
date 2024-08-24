import json
import requests
from enum import Enum
from dataclasses import dataclass


class SurflineType(str, Enum):
    RATING = "rating"
    WAVE = "wave"
    WIND = "wind"
    TIDES = "tides"
    WEATHER = "weather"


class SurflineParameter(str, Enum):
    SPOTID = "spotId"
    DAYS = "days"
    INTERVAL_HOURS = "intervalHours"
    MAX_HEIGHTS = "maxHeights"
    LOTUS = "sds"
    ACCESS_TOKEN = "accesstoken"


class SurflineOptimalScore(Enum):
    SUBOPTIMAL = 0
    GOOD = 1
    OPTIMAL = 2


@dataclass
class SurflineSpot:
    id: int``
    name: str
    lat: float
    lon: float


def _create_mapview_url(polygon: list[list[list[float]]]):
    """
    Create a mapview url from a polygon.

    Parameters
    ----------
    polygon : list[list[list[float]]]
        A list of polygons, where each polygon is a list of points, where each point is a list of two floats representing the latitude and longitude.

    Returns
    -------
    str
        A surfline url.```
    """
    longitude = [
        point[0]
        for poly in polygon
        for point in poly
    ]
    latitude = [
        point[1]
        for poly in polygon
        for point in poly
    ]

    north = max(latitude)
    south = min(latitude)
    east = max(longitude)
    west = min(longitude)

    base_url = "https://services.surfline.com/kbyg/mapview"

    return f"{base_url}?north={north}&south={south}&east={east}&west={west}"


def _create_forecast_url(forecast: SurflineType, params: dict[SurflineParameter, int | str]):
    param_string = '&'.join(
        [
            f"{k}={v}"
            for k,v in params.items()
        ]
    )
    base_url = "https://services.surfline.com/kbyg/spots/forecasts"
    return f"{base_url}/{forecast}?{param_string}"


def get_spots(polygon: list[list[list[float]]]):
    url = _create_mapview_url(polygon)
    
    resp = requests.get(url)
    if not resp.ok:
        raise RuntimeError(f"Failed to get mapview: {resp.status_code}")
    
    data = json.loads(resp.content.decode('utf-8'))
    spots = [
        SurflineSpot(
            id=spot["_id"],
            name=spot["name"],
            lat=spot["lat"],
            lon=spot["lon"]
        )
        for spot in data["data"]["spots"]
    ]
    return spots


def get_forecast(spot: str):
    for forecast in SurflineType:
        url = _create_forecast_url(
            forecast=forecast.value,
            params={
                SurflineParameter.SPOTID: spot,
            }
        )

