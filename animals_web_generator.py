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
    """ Build an animals string in HTML form """
    output = ""

    for animal in data:
        output += '<li class="cards__item">\n'
        output += '  <div class="card__title">'

        if "name" in animal:
            output += f"{animal['name']}"
        else:
            output += "Unbekanntes Tier"

        output += '</div>\n'
        output += '  <div class="card__text">\n'

        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output += f"Ernährung: {animal['characteristics']['diet']}<br>\n"

        if "locations" in animal and len(animal["locations"]) > 0:
            output += f"Ort: {animal['locations'][0]}<br>\n"

        if "characteristics" in animal and "type" in animal["characteristics"]:
            output += f"Typ: {animal['characteristics']['type']}<br>\n"

        output += "  </div>\n"
        output += "</li>\n"

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
