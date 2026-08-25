import json

def load_data(file_path):
    """ Load a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def load_templates(template_path):
    """ Load the HTML templates """
    with open(template_path, "r", encoding="utf-8") as handle:
        return handle.read()


def build_animals_string(data):
    output = ""

    for animal in data:
        output += '<li class="cards__item">\n'

        # Titel
        name = animal.get("name", "Unbekanntes Tier")
        output += f'  <div class="card__title">{name}</div>\n'

        # Textblock starten
        output += '  <p class="card__text">\n'

        # Ernährung
        diet = animal.get("characteristics", {}).get("diet")
        if diet:
            output += f'      <strong style="color:#444;">Diet:</strong> {diet}<br/>\n'

        # Ort
        locations = animal.get("locations", [])
        if locations:
            output += f'      <strong style="color:#444;">Location:</strong> {locations[0]}<br/>\n'

        # Typ
        type_ = animal.get("characteristics", {}).get("type")
        if type_:
            output += f'      <strong style="color:#444;">Type:</strong> {type_}<br/>\n'

        output += '  </p>\n'
        output += '</li>\n'

    return output



def write_output(html_content, output_path):
    """ Write an HTML output """
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(html_content)

# ---------------------
# Hauptprogramm
# ---------------------

animals = load_data("animals_data.json")
template = load_templates("animals_template.html")

animals_string = build_animals_string(animals)

final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_string)

write_output(final_html, "animals.html")
