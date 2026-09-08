import requests

def load_data_from_api(tiername, api_key):
    """ Holt Tierdaten von der API-Ninjas Animals API """
    url = f"https://api.api-ninjas.com/v1/animals?name={tiername}"
    headers = {"X-Api-Key": api_key}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Fehler beim Abrufen der API:", response.status_code)
        return []

    return response.json()


def load_templates(template_path):
    """ Load the HTML templates """
    with open(template_path, "r", encoding="utf-8") as handle:
        return handle.read()


def serialize_animal(animal):
    name = animal.get("name", "Unbekanntes Tier")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations", [])
    type_ = animal.get("characteristics", {}).get("type")

    html = []
    html.append('<li class="cards__item">')
    html.append(f'  <div class="card__title">{name}</div>')
    html.append('  <div class="card__text">')
    html.append('    <ul class="animal-details">')

    if diet:
        html.append(f'      <li class="animal-detail"><strong>Diet:</strong> {diet}</li>')

    if locations:
        html.append(f'      <li class="animal-detail"><strong>Location:</strong> {locations[0]}</li>')

    if type_:
        html.append(f'      <li class="animal-detail"><strong>Type:</strong> {type_}</li>')

    html.append('    </ul>')
    html.append('  </div>')
    html.append('</li>')

    return "\n".join(html)


def build_animals_string(data):
    return "\n".join(serialize_animal(animal) for animal in data)


def write_output(html_content, output_path):
    """ Write an HTML output """
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(html_content)


# ---------------------
# Hauptprogramm
# ---------------------

api_key = "JhHpehCghmuA5akW8Jal2GvlzbuEtzsbdCIFFnrv"

# Statt JSON-Datei → API-Abfrage
animals = load_data_from_api("fox", api_key)

template = load_templates("animals_template.html")

animals_string = build_animals_string(animals)

final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_string)

write_output(final_html, "animals.html")


