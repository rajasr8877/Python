from jsonschema import validate, ValidationError,SchemaError
from marshmallow import Schema, fields, pprint
from flask import Flask, jsonify
# import OlympusPOC.InvDevice.Schema.ProcedureDataCalss as ProcedureDataCalss
# import 
from OlympusPOC.InvDevice.Schema.ProcedureDataCalss import Procedure
# from LabResultsSchema import LabResultsSchema


app = Flask(__name__)


class ProcedureSchema(Schema):
    laser_system_serial_number = fields.Str(required=True)
    case_number = fields.Str(required=True)
    procedure_date = fields.Date(required=True)
    ecm_logs = fields.Str(allow_none=True)

procedure_schema = ProcedureSchema()

@app.route('/procedureDetails', methods=['GET'])
def get_users():
    procedure = Procedure(
        laser_system_serial_number="ABC123",
        case_number="XYZ-456",
        procedure_date="2024-04-09",
        ecm_logs="Log data goes here"
    )
    return jsonify(procedure.__dict__)
    # try:
    #     loaded_data, errors = procedure_schema.load(data)
    #     return jsonify(loaded_data)
    # except ValidationError as e:
    #     return jsonify({'error': str(e)}), 400
    # except SchemaError as e:
    #     errors = e.messages
        # return jsonify({'error': errors}), 400
        

if __name__ =='__main__':
    app.run(debug=True)
