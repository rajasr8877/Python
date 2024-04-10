from jsonschema import validate, ValidationError,SchemaError
from marshmallow import Schema, fields, pprint
from flask import Flask, jsonify

import sys
sys.path.insert(0,'C:\\Raja\\Olympus\\Dev\\Workspace\\Python\\POC\\InvDevice\\Schema')
sys.path.insert(1,'C:\\Raja\\Olympus\\Dev\\Workspace\\Python\\POC\\InvDevice\\Service')
from Procedure import Procedure
from LabResults import LabResults
from DemographicInformation import DemographicInformation
from LabResultsSpecifics import LabResultsSpecifics
from ProcedureDTO import ProcedureDTO
from ProcedureServiceImpl import ProcedureServiceImpl

app = Flask(__name__)


class ProcedureSchema(Schema):
    laser_system_serial_number = fields.Str(required=True)
    case_number = fields.Str(required=True)
    procedure_date = fields.Date(required=True)
    ecm_logs = fields.Str(allow_none=True)

procedure_schema = ProcedureSchema()
# lap_resul_schema = LabResultsSchema()

@app.route('/procedureDetails', methods=['GET'])
def getProcedureDetails():
    procedure = createProcedureObject()
    procedureDto = ProcedureDTO(procedureDTO=[procedure])
   
    # procedureServiceImpl = ProcedureServiceImpl()
    # procedureDto = procedureServiceImpl.getProcedureDetailFromDAO() : ProcedureDTO;
    return jsonify(procedureDto.__dict__)
    # return procedureServiceImpl

def createProcedureObject():
    lap_resul_schema = LabResults(file_type="csv",content="TetstContent");
    lab_result_specifics = LabResultsSpecifics(
        stone_composition="test_stone_Composition",tissue_composition="test_tissue_composition"
    )
    demographic_info = DemographicInformation(year_of_birth="10/02/1998",ethnicity="test_ethnicity",gender="male")
    
    procedure = Procedure(
        laser_system_serial_number="ABC123",
        case_number="XYZ-456",
        procedure_date="2024-04-09",
        ecm_logs="Log data goes here",
        lab_results=lap_resul_schema,
        endoscopic_used=True,
        surgical_videos="urlOfSurgical_videos",
        fiber_used="test_fiber_used",
        laser_source_information="test_laser_source_information",
        imaging_mode="test_imaging_mode",
        light_source_lamp_age="10",
        number_of_stones_treated=20,
        stone_burden="test_stone_burden",
        treatment_location="chennai",
        treatment_type="test_fever",
        demographic_information=demographic_info,
        lab_results_specifics=lab_result_specifics
    )
    
    return procedure
    # loaded_data = procedure_schema.load(data)
    # print(loaded_data)
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
