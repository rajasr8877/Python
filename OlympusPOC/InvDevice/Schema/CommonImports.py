# from jsonschema import validate, ValidationError
# from marshmallow import Schema, fields, pprint
# from flask import Flask, jsonify


    # data = {
    # "laser_system_serial_number": "ABC123",
    # "case_number": "XYZ-456",
    # "procedure_date": "2024-04-09",
    # "ecm_logs": "Log data goes here"
    # }

import os

# Get the path of the current file
current_file_path = os.path.abspath(__file__)

# Extract the root path from the current file path
root_path = os.path.dirname(os.path.dirname(current_file_path))

print(root_path)
# Add the root path to sys.path
# sys.path.insert(0, root_path)