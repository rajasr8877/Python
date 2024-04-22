from marshmallow import Schema, fields

class LaserSourceInformationSchema(Schema):
    code = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()

class ImagingModeSchema(Schema):
    code = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()

class SpecificSchema(Schema):
    code = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()

class TreatmentTypesSchema(Schema):
    code = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()

class TreatmentLocationSchema(Schema):
    code = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()

# class TreatmentLocationTypesSchema(Schema):
#     treatment_location = fields.List(fields.Nested('TreatmentLocationSchema', many=False, load_only=True))
#     treatment_type = fields.List(fields.Nested('TreatmentTypeSchema', many=False, load_only=True))

# class TreatmentLocationSpecificsSchema(Schema):
#     specific = fields.List(fields.Nested('SpecificSchema', many=False, load_only=True))
#     treatment_location = fields.List(fields.Nested('TreatmentLocationSchema', many=False, load_only=True))



class MainSchema(Schema):
    LaserSourceInformation = fields.List(fields.Nested(LaserSourceInformationSchema))
    ImagingMode = fields.List(fields.Nested(ImagingModeSchema))
    TreatmentTypes = fields.List(fields.Nested(TreatmentTypesSchema))
    TreatmentLocationTypes = fields.List(fields.Nested(TreatmentLocationSchema))