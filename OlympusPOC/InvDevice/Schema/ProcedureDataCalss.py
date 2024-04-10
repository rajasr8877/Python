from dataclasses import dataclass

@dataclass
class Procedure:
    laser_system_serial_number: str
    case_number: str
    procedure_date: str
    ecm_logs: str