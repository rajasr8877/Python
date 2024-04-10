
from dataclasses import dataclass
from Procedure import Procedure
from typing import List

@dataclass
class ProcedureDTO:
    procedureDTO:List[Procedure]
