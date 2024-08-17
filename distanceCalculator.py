import geopy
from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import certifi


@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude


def get_coordinates(address: str) -> Coordinates | None:
    geolocator = Nominatim(user_agent="distance_calculator_app/1.0", scheme="https")

    # Use certifi's certificate bundle
    geolocator.adapter.session.verify = certifi.where()

    try:
        location = geolocator.geocode(address)
        if location:
            print(f"Geocoded '{address}' to coordinates: ({location.latitude}, {location.longitude})")
            return Coordinates(latitude=location.latitude, longitude=location.longitude)
        else:
            print(f"Failed to geocode address: {address}")
    except Exception as e:
        print(f"Error geocoding address '{address}': {e}")

    return None


def calculate_distance(home: Coordinates, target: Coordinates) -> float | None:
    if home and target:
        distance: float = geodesic(home.coordinates(), target.coordinates()).mi
        return distance


def get_distance(home: str, target: str) -> float | None:
    home_coordinates: Coordinates = get_coordinates(home)
    target_coordinates: Coordinates = get_coordinates(target)

    if home_coordinates and target_coordinates:
        if distance := calculate_distance(home_coordinates, target_coordinates):
            print(f'{home} -> {target}')
            print(f'{distance:.2f} miles')
            return distance
    else:
        print('Failed to calculate the distance.')


def main():
    home: str = 'Orlando FL'
    print(f'Home address: {home}')

    target: str = input('Enter an address: ')
    print('Calculating...')
    get_distance(home, target)


if __name__ == '__main__':
    main()
