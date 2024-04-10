from dataclasses import dataclass
from LabResults import LabResults
from DemographicInformation import DemographicInformation
from LabResultsSpecifics import LabResultsSpecifics

@dataclass
class Procedure:
    laser_system_serial_number: str
    case_number: str
    procedure_date: str
    ecm_logs: str
    lab_results: LabResults
    surgical_videos:str
    endoscopic_used : bool
    laser_source_information:str
    light_source_lamp_age:str
    imaging_mode :str
    treatment_location :str
    treatment_type :str
    fiber_used :str
    number_of_stones_treated :int
    stone_burden :str
    lab_results_specifics:LabResultsSpecifics
    demographic_information:DemographicInformation