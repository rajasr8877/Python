from marshmallow import Schema, fields

class LaserSourceInformationSchema(Schema):
    code = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()

class ImagingModeSchema(Schema):
    code = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()


class TreatmentLocationSchema(Schema):
    code = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()
    treatment_types = fields.Nested('TreatmentTypesSchema', many=True)
    specifics = fields.Nested('SpecificSchema', many=True)

class SpecificSchema(Schema):
    code = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()
    # treatment_location_types = fields.Nested('TreatmentLocationSchema', many=True, exclude=('specifics', 'treatment_types'))

class TreatmentTypesSchema(Schema):
    code = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()
    # treatment_location_types = fields.Nested('TreatmentLocationSchema', many=True, exclude=('treatment_types', 'specifics'))
    # specifics = fields.Nested(SpecificSchema, many=True)



# class TreatmentLocationTypesSchema(Schema):
#     treatment_location = fields.List(fields.Nested('TreatmentLocationSchema', many=False, load_only=True))
#     treatment_type = fields.List(fields.Nested('TreatmentTypeSchema', many=False, load_only=True))

# class TreatmentLocationSpecificsSchema(Schema):
#     specific = fields.List(fields.Nested('SpecificSchema', many=False, load_only=True))
#     treatment_location = fields.List(fields.Nested('TreatmentLocationSchema', many=False, load_only=True))



class MainSchema(Schema):
    LaserSourceInformation = fields.List(fields.Nested(LaserSourceInformationSchema))
    ImagingMode = fields.List(fields.Nested(ImagingModeSchema))
    # TreatmentTypes = fields.List(fields.Nested(TreatmentTypesSchema))
    TreatmentLocationTypes = fields.List(fields.Nested(TreatmentLocationSchema))