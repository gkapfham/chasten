"""Validate various aspects of configurations and command-line arguments."""

from typing import Tuple

from jsonschema import Draft7Validator
from jsonschema.exceptions import ValidationError

from chasten import constants

JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "chasten": {
            "type": "object",
            "properties": {
                "verbose": {"type": "boolean"},
                "debug_level": {
                    "type": "string",
                    "enum": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                },
            },
            "additionalProperties": False,
        },
    },
}

def validate_configuration(configuration) -> Tuple[bool, str]:
    """Validate the configuration."""
    try:
        validator = Draft7Validator(JSON_SCHEMA)
        validator.validate(configuration, JSON_SCHEMA)
        return (True, constants.markers.Empty)
    except ValidationError as validation_error:
        error_message = str(validation_error)
        return (False, error_message)