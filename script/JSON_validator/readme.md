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

  ```bash
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
```

## Usage

1. **Execute the script:**

   ```bash
   python3 presentation_definition_validator.py schema.json example_to_test.json

**Check the output:**

You can get different kind of errors, these are just some of them:

![Error 1](script/JSON_validator/err1.png)

![Error 2](script/JSON_validator/err2.png)

![Error 3](script/JSON_validator/err3.png)

![Error 4](script/JSON_validator/err4.png)

![Error 5](script/JSON_validator/err5.png)


2.. **Final result:**

After some modification i got a JSON like this:

  ```json
{
  "presentation_definition": {
    "id": "presentation definitions",
    "input_descriptors": [
      {
        "id": "eu.europa.ec.eudiw.pid.it.1",
        "name": "Person Identification Data",
        "purpose": "User authentication",
        "group": ["group1"],
        "format": {
          "vc+sd-jwt": {
            "alg": ["RS256", "ES256"]
          }
        },
        "constraints": {
          "limit_disclosure": "preferred",
          "fields": [
            {
              "path": ["$.credentialSubject.unique_id"],
              "filter": {
                "type": "string",
                "const": "unique_id"
              }
            },
            {
              "path": ["$.credentialSubject.given_name"],
              "filter": {
                "type": "string",
                "const": "given_name"
              }
            },
            {
              "path": ["$.credentialSubject.family_name"],
              "filter": {
                "type": "string",
                "const": "family_name"
              }
            }
          ]
        }
      },
      {
        "id": "WalletAttestation",
        "name": "Wallet Attestation",
        "purpose": "Wallet Authentication",
        "group": ["group1"],
        "format": {
          "jwt": {
            "alg": ["RS256", "ES256"]
          }
        },
        "constraints": {
                "limit_disclosure": "preferred",
          "fields": [
            {
              "path": ["$.iss"],
              "filter": {
                "type": "string",
                "const":"https://issuer.example.org"
              }
            },
            {
              "path": ["$.exp"],
              "filter": {
                "type": "string",
                "const": 1504700136
              }
            },
            {
              "path": ["$.iat"],
              "filter": {
                "type": "string",
                "const": 1504700136
              }
            },
            {
              "path": ["$.cnf.jwk"],
              "filter": {
                      "type": "string"
              }
            },
            {
              "path": ["$.aal"],
              "filter": {
                "type": "string",
                "const": "aal"
              }
            }
          ]
        }
      }
    ],
    "submission_requirements": [
      {
        "name": "Sample requirement",
        "rule": "pick",
        "count": 1,
        "from": "group1"
      }
    ]
  }
}
```

![Final](script/JSON_validator/end.png)


