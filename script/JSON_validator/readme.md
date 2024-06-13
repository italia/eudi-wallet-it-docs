# Presentation Definition JSON Validator

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)

## Introduction

This script is designed to validate JSON data against a specified JSON schema and additional custom rules. It reads the JSON schema and data from files, checks if the data conforms to the schema, and ensures that certain additional requirements are met.
This validation process helps in ensuring that the JSON data structure adheres to expected standards and rules, making it reliable and consistent for further processing or usage in applications.

## Installation

To get started with this project, follow these steps:

1. **Download the files:**

   ```bash
   python script
   schema.json

2. **Create a presentation_definition JSON file:**

This is just an example:

  ```json
{
  "presentation_definition": {
    "id": "presentation definitions",
    "input_descriptors": [
      {
        "id": "eu.europa.ec.eudiw.pid.it.1",
        "name": "Person Identification Data",
        "purpose": "User authentication",
        "format": "vc+sd-jwt",
        "constraints": {
          "fields": [
            {
              "path": [
                "$.credentialSubject.unique_id",
                "$.credentialSubject.given_name",
                "$.credentialSubject.family_name"
              ]
            }
          ],
          "limit_disclosure": "preferred"
        }
      },
      {
        "id": "WalletAttestation",
        "name": "Wallet Attestation",
        "purpose": "Wallet Authentication",
        "format": "jwt",
        "constraints": {
          "fields": [
            {
              "path": [
                "$.iss",
                "$.exp",
                "$.iat",
                "$.cnf.jwk",
                "$.aal"
              ]
            }
          ]
        }
      }
    ]
  }
}

3. **Execute the script:**

   ```bash
   python3 presentation_definition_validator.py schema.json example_to_test.json

4. **Check the output:**


5. **Final result:**



