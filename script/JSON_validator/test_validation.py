import json
from pydantic import ValidationError
from model import PresentationDefinitionForAHighAssuranceProfile

# Function to load JSON data from a file
def load_json(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)

# Load valid data from JSON file and create an instance of PresentationDefinitionForAHighAssuranceProfile
try:
    valid_data = load_json('example_data.json')
    presentation_definition_instance = PresentationDefinitionForAHighAssuranceProfile(**valid_data)
    
    # Print the ID of the presentation definition
    print(f"Presentation ID: {presentation_definition_instance.presentation_definition.id}")
    
    # Print the name of the first input descriptor
    print(f"Input Descriptor Name: {presentation_definition_instance.presentation_definition.input_descriptors[0].name}")
except ValidationError as e:
    # Handle and print validation errors
    print(f"Validation error: {e}")
