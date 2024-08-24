import json
import requests
from dataclasses import dataclass


@dataclass
class SurflineSpot:
    id: int
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
        A surfline url.
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


if __name__ == "__main__":
    dune_road_coords = [
        [
            [
                -72.74354223091918,
                40.790407420490396
            ],
            [
                -72.74354223091918,
                40.75732942240188
            ],
            [
                -72.66676167490857,
                40.75732942240188
            ],
            [
                -72.66676167490857,
                40.790407420490396
            ],
            [
                -72.74354223091918,
                40.790407420490396
            ]
        ]
    ]

    spots = get_spots(dune_road_coords)

    for spot in spots:
        print(spot.name)