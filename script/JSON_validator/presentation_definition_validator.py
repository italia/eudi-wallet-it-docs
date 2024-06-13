import json
import jsonschema
import argparse
from jsonschema import validate, ValidationError

# Function to read a JSON file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Function to validate additional rules
def validate_additional_rules(data):
    presentation_definition = data.get('presentation_definition', {})

    # Rule 1: Required properties in presentation_definition
    required_pd_properties = ['id', 'input_descriptors', 'submission_requirements']
    for prop in required_pd_properties:
        if prop not in presentation_definition:
            raise ValidationError(f"Missing required property '{prop}' in presentation_definition")

    # Rule 2: Required properties in input_descriptors
    for descriptor in presentation_definition.get('input_descriptors', []):
        required_id_properties = ['id', 'name', 'purpose', 'group', 'format', 'constraints']
        for prop in required_id_properties:
            if prop not in descriptor:
                raise ValidationError(f"Missing required property '{prop}' in input_descriptors")

        # Rule 3: Required properties in constraints
        constraints = descriptor.get('constraints', {})
        required_constraints_properties = ['limit_disclosure', 'fields']
        for prop in required_constraints_properties:
            if prop not in constraints:
                raise ValidationError(f"Missing required property '{prop}' in constraints")

        # Rule 4: Required properties in fields
        for field in constraints.get('fields', []):
            required_fields_properties = ['path', 'filter']
            for prop in required_fields_properties:
                if prop not in field:
                    raise ValidationError(f"Missing required property '{prop}' in fields")

            # Rule 5: Only one path with a static path
            if len(field['path']) != 1:
                raise ValidationError("Field 'path' must contain exactly one entry")

            # Rule 6: Filter must only contain string and const elements
            filter_keys = field['filter'].keys()
            if any(key not in ['type', 'const'] for key in filter_keys):
                raise ValidationError("Filter must only contain 'type' and 'const' elements")
            if field['filter'].get('type') != 'string':
                raise ValidationError("Filter 'type' must be 'string'")

    # Rule 7: Required properties in submission_requirements
    for submission in presentation_definition.get('submission_requirements', []):
        required_sr_properties = ['name', 'rule', 'count', 'from']
        for prop in required_sr_properties:
            if prop not in submission:
                raise ValidationError(f"Missing required property '{prop}' in submission_requirements")
        if submission['rule'] != 'pick':
            raise ValidationError("Submission rule must be 'pick'")

# Function to validate data
def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
        print("JSON schema validation passed.")

        # Validate additional rules
        validate_additional_rules(data)
        print("Additional rules validation passed.")

        return True
    except ValidationError as err:
        print("JSON data is invalid.")
        print(err)
        return False

# Main function
def main(schema_file, data_file):
    # Load schema and data from files
    schema = load_json(schema_file)
    data = load_json(data_file)

    # Validate data
    validate_json(data, schema)

# Command-line argument configuration
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate JSON data against a schema")
    parser.add_argument("schema", help="Path to the JSON schema file")
    parser.add_argument("data", help="Path to the JSON data file")

    args = parser.parse_args()
    main(args.schema, args.data)
