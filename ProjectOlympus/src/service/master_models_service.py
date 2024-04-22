

from src.models.master.master_table_models import ImagingModeModel, LaserSourceInfoModel, TreatmentTypeModel, TreatmentLocationModel

class MasterModelService:

    @staticmethod
    def get_all_master_model_details() -> dict:
        result = dict()
        laser_source_info = LaserSourceInfoModel.query.filter(LaserSourceInfoModel.isActive).all()
        imaging_mode_info = ImagingModeModel.query.filter(ImagingModeModel.isActive).all()
        # treatment_type_info = TreatmentTypeModel.query.filter(TreatmentTypeModel.isActive).all()
        treatment_location_type = TreatmentLocationModel.query.filter(TreatmentLocationModel.isActive).all()
        result.update({"ImagingMode": imaging_mode_info})
        result.update({"LaserSourceInformation": laser_source_info})
        # result.update({"TreatmentTypes": treatment_type_info})
        result.update({"TreatmentLocationTypes": treatment_location_type})
        return result