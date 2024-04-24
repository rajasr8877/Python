from .base_model import BaseModel, BaseColumnModel
from db import db


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


class TreatmentLocationTypesModel(BaseColumnModel):
    __tablename__ = "treatment_location_types"
    isActive = db.Column(db.Boolean, default=True)
    treatment_location_id = db.Column(
        db.Integer, db.ForeignKey("treatment_location.id")
    )
    treatment_type_id = db.Column(db.Integer, db.ForeignKey("treatment_type.id"))


class TreatmentLocationSpecificsModel(BaseColumnModel):
    __tablename__ = "treatment_location_specifics"
    specific_id = db.Column(db.Integer, db.ForeignKey("specific.id"))
    treatment_location_id = db.Column(
        db.Integer, db.ForeignKey("treatment_location.id")
    )


class TreatmentLocationModel(BaseModel):
    __tablename__ = "treatment_location"
    treatment_types = db.relationship(
        "TreatmentTypeModel",
        secondary="treatment_location_types",
        back_populates="treatment_location_types",
    )
    specifics = db.relationship(
        "SpecificModel",
        secondary="treatment_location_specifics",
        back_populates="treatment_location_types",
    )


class TreatmentTypeModel(BaseModel):
    __tablename__ = "treatment_type"
    treatment_location_types = db.relationship(
        "TreatmentLocationModel",
        secondary="treatment_location_types",
        back_populates="treatment_types",
        lazy=True,
    )


class SpecificModel(BaseModel):
    __tablename__ = "specific"
    treatment_location_types = db.relationship(
        "TreatmentLocationModel",
        secondary="treatment_location_specifics",
        back_populates="specifics",
        lazy=True,
    )


class FileTypeModel(BaseModel):
    __tablename__ = "file_type"


class EventTypeModel(BaseModel):
    __tablename__ = "event_type"


class IdentifierModel(BaseModel):
    __tablename__ = "identifier"


class RoleTypeModel(BaseModel):
    __tablename__ = "role_type"


class LabReportTypeModel(BaseModel):
    __tablename__ = "lab_report_type"


class MLModel(BaseModel):
    __tablename__ = "ml_model"


class FeatureEnggModel(BaseModel):
    __tablename__ = "feature_engg"


class DataSelectionModel(BaseModel):
    __tablename__ = "data_selection"


class MetadataAttributeModel(BaseModel):
    __tablename__ = "metadata_attribute"