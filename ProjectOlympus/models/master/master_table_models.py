from .base_model import BaseModel

class LaserSourceInfoModel(BaseModel):
    __tablename__ = "laser_source_information"

class EthnicityModel(BaseModel):
    __tablename__ = "ethnicity"

class FiberUsedModel(BaseModel):
    __tablename__ = "fiber_used"

class ImagingModeModel(BaseModel):
    __tablename__ = "imaging_mode"