from flask.views import MethodView
from flask_smorest import Blueprint
from src.service.master_models_service import MasterModelService as mService
from src.schemas.master.config_schema import MainSchema


blp = Blueprint("ConfigApi", "Config", description="Get All master table related details")


@blp.route("/config")
class MasterConfigApi(MethodView):
    @blp.response(200, MainSchema())
    def get(self):        
        return mService.get_all_master_model_details()