from jsonschema import validate, ValidationError
from marshmallow import Schema, fields, pprint
from flask import Flask, jsonify
from LabResults import LabResultsSchema

# class LabResultsSchema(Schema):
#     file_type = fields.Str(required=True)
#     content = fields.Str(allow_none=True)

class ProcedureSchema(Schema):
    laser_system_serial_number = fields.Str(required=True)
    case_number = fields.Str(required=True)
    procedure_date = fields.Date(required=True)
    lab_results = fields.Nested(LabResultsSchema, required=True)
    ecm_logs = fields.Str(allow_none=True)
    solitive_logs = fields.Str(allow_none=True)
    surgical_videos = fields.List(fields.Nested({
        "url": fields.Str(),
        "file_name": fields.Str()
    }))
    endoscopic_used = fields.Bool(allow_none=True)
    laser_source_information = fields.Str(allow_none=True)
    light_source_lamp_age = fields.Str(allow_none=True)
    imaging_mode = fields.Str(allow_none=True)
    treatment_location = fields.Str(allow_none=True)
    treatment_type = fields.Str(allow_none=True)
    fiber_used = fields.Str(allow_none=True)
    number_of_stones_treated = fields.Integer(allow_none=True)
    stone_burden = fields.Str(allow_none=True)
    demographic_information = fields.Nested({
        "year_of_birth": fields.Integer(),
        "ethnicity": fields.Str(),
        "gender": fields.Str()
    }, required=True)
    lab_results_specifics = fields.Nested({
        "stone_composition": fields.Str(),
        "tissue_composition": fields.Str()
    }, allow_none=True)

def get_procedure_data(json_data):
    schema = ProcedureSchema()
    try:
        validated_data = schema.load(json_data)
        return validated_data
    except ValidationError as e:
        print(f"Validation error: {e.message}")
        return None

# Example usage
json_data = {
    "laser_system_serial_number": "12345",
    "case_number": "67890",
    "procedure_date": "2023-04-08",
    "lab_results": {
        "file_type": "pdf",
        "content": "base64_encoded_content"
    },
    "demographic_information": {
        "year_of_birth": 1990,
        "ethnicity": "Asian",
        "gender": "Male"
    }
}

procedure_data = get_procedure_data(json_data)
if procedure_data is not None:
    pprint(procedure_data)