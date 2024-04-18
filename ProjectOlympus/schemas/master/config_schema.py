from marshmallow import Schema, fields

class LaserSourceInformationSchema(Schema):
    code = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()

class ImagingModeSchema(Schema):
    code = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()

class TreatmentTypesSchema(Schema):
    code = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()

class MainSchema(Schema):
    LaserSourceInformation = fields.List(fields.Nested(LaserSourceInformationSchema))
    ImagingMode = fields.List(fields.Nested(ImagingModeSchema))
    # TreatmentTypes = fields.List(fields.Nested(TreatmentTypesSchema))
    # TreatmentLocationTypes = fields.List(fields.Nested(TreatmentLocationTypesSchema))