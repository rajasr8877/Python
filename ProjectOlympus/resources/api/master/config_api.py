from flask.views import MethodView
from flask_smorest import Blueprint

from schemas.master.config_schema import MainSchema
from models.master.master_table_models import LaserSourceInfoModel, ImagingModeModel
# from sqlalchemy.exc import SQLAlchemyError

# from db import db
# from models import LaserSourceInfoModel,EthnicityModel,ImagingModeModel,FiberUsedModel

blp = Blueprint("Items", "items", description="Operations on items")

@blp.route("/config")
class MasterConfigApi(MethodView):
    @blp.response(200, MainSchema())
    def get(self):
        laser_source_info = LaserSourceInfoModel.query.all()
        imaging_mode_info = ImagingModeModel.query.all()  # Assuming you have a model named ImagingModeModel
        return {"LaserSourceInformation": laser_source_info, "ImagingMode": imaging_mode_info}