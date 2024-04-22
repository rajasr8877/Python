from flask.views import MethodView
from flask_smorest import Blueprint
from src.models.master.master_table_models import ImagingModeModel, LaserSourceInfoModel
from src.schemas.master.config_schema import MainSchema

# from sqlalchemy.exc import SQLAlchemyError

# from db import db
# from models import LaserSourceInfoModel,EthnicityModel,ImagingModeModel,FiberUsedModel

blp = Blueprint("Items", "items", description="Operations on items")


@blp.route("/config")
class MasterConfigApi(MethodView):
    @blp.response(200, MainSchema())
    def get(self):
        result = dict()
        laser_source_info = LaserSourceInfoModel.query.all()
        imaging_mode_info = ImagingModeModel.query.all()
        result.update({"ImagingMode": imaging_mode_info})
        result.update({"LaserSourceInformation": laser_source_info})
        return result