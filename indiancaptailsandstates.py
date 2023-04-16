2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
import json

# Define the dictionary of Indian states and capitals
indian_states_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Uttar Pradesh": "Lucknow",
    "West Bengal": "Kolkata"
}

# Write the dictionary into a JSON file
with open("indian_states_capitals.json", "w") as json_file:
    json.dump(indian_states_capitals, json_file)

print("Indian states and capitals written to indian_states_capitals.json")
print(type(indian_states_capitals))