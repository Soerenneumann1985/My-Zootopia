import json

def load_data(file_path):
    """ Load a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def print_animals(data):
    """ Print selected fields for each animal """
    for animal in data:
        print("-----")

        # Name
        if "name" in animal:
            print("Name:", animal["name"])

        # Ernährung (diet)
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            print("Ernährung:", animal["characteristics"]["diet"])

        # Erster Ort
        if "locations" in animal and len(animal["locations"]) > 0:
            print("Ort:", animal["locations"][0])

        # Typ
        if "characteristics" in animal and "type" in animal["characteristics"]:
            print("Typ:", animal["characteristics"]["type"])

# Programm starten
animals = load_data("animals_data.json")
print_animals(animals)