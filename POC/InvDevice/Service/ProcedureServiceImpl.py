import sys
sys.path.insert(0,'C:\\Raja\\Olympus\\Dev\\Workspace\\Python\\POC\\InvDevice\\Schema')
from Procedure import Procedure
from LabResults import LabResults
from DemographicInformation import DemographicInformation
from LabResultsSpecifics import LabResultsSpecifics
from ProcedureDTO import ProcedureDTO
from flask import Flask, jsonify

app = Flask(__name__)

class ProcedureServiceImpl:
    def getProcedureDetailFromDAO():

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

        procedureDto = ProcedureDTO(procedureDTO=[procedure])
    
        return procedureDto
    
    