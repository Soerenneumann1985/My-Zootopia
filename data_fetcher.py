import requests

api_key = "JhHpehCghmuA5akW8Jal2GvlzbuEtzsbdCIFFnrv"

def fetch_data(animal_name, api_key):
    """Wrapper-Funktion, die einfach load_data_from_api aufruft."""
    return load_data_from_api(animal_name, api_key)

def load_data_from_api(tiername, api_key):
    """Holt Tierdaten von der API-Ninjas Animals API."""
    url = f"https://api.api-ninjas.com/v1/animals?name={tiername}"
    headers = {"X-Api-Key": api_key}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Fehler beim Abrufen der API:", response.status_code)
        return []

    return response.json()
