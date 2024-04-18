from .base_model import BaseModel


class LaserSourceInfoModel(BaseModel):
    __tablename__ = "laser_source_information"


class EthnicityModel(BaseModel):
    __tablename__ = "ethnicity"


class FiberUsedModel(BaseModel):
    __tablename__ = "fiber_used"


class ImagingModeModel(BaseModel):
    __tablename__ = "imaging_mode"


class GenderModel(BaseModel):
    __tablename__ = "gender"


class LaserSerialNumberModel(BaseModel):
    __tablename__ = "laser_serial_number"


class TreatmentLocationModel(BaseModel):
    __tablename__ = "treatment_location"


class TreatmentTypeModel(BaseModel):
    __tablename__ = "treatment_type"


class SpecificModel(BaseModel):
    __tablename__ = "specific"


class FileTypeModel(BaseModel):
    __tablename__ = "file_type"


class EventTypeModel(BaseModel):
    __tablename__ = "event_type"