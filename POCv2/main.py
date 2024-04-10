import datetime
from datetime import UTC
from uuid import uuid4
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# from flasgger import Swagger, swag_from
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
# swagger = Swagger(app)

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(base_url=SWAGGER_URL, api_url=API_URL, config={
    'app_name': 'Procedure Access API'
})

app.register_blueprint(blueprint=swagger_ui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/', methods=['GET'])
def home():
    name = "Raja"
    return jsonify({'msg': 'Wellcome '+name+' to Procedure app'})


basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +  os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class ProcedureDetails(db.Model):
    __tablename__ = "procedures"
    id = db.Column(db.Integer, primary_key=True)
    laser_system_serial_number = db.Column(db.String(100),nullable=False)
    case_number = db.Column(db.String(100), nullable=False)
    procedure_date = db.Column(db.String(100), nullable=False)
    ecm_logs = db.Column(db.String(100), nullable=False)
    surgical_videos = db.Column(db.String(100), nullable=False)
    endoscopic_used = db.Column(db.String(100), nullable=False)
    laser_source_information = db.Column(db.String(100), nullable=False)
    light_source_lamp_age = db.Column(db.String(100), nullable=False)
    imaging_mode = db.Column(db.String(100), nullable=False)
    treatment_location = db.Column(db.String(100), nullable=False)
    treatment_type = db.Column(db.String(100), nullable=False)
    fiber_used = db.Column(db.String(100), nullable=False)
    number_of_stones_treated = db.Column(db.Integer, nullable=False)
    stone_burden = db.Column(db.String(100), nullable=False)

    def __init__(self, laser_system_serial_number,case_number, procedure_date, ecm_logs, surgical_videos, endoscopic_used, laser_source_information, light_source_lamp_age, imaging_mode, treatment_location, treatment_type, fiber_used, number_of_stones_treated, stone_burden):
       self.laser_system_serial_number = laser_system_serial_number
       self.case_number = case_number
       self.procedure_date = procedure_date
       self.ecm_logs = ecm_logs
       self.surgical_videos = surgical_videos
       self.endoscopic_used = endoscopic_used
       self.laser_source_information = laser_source_information
       self.light_source_lamp_age =light_source_lamp_age
       self.imaging_mode =imaging_mode
       self.treatment_location = treatment_location
       self.treatment_type= treatment_type
       self.fiber_used = fiber_used
       self.number_of_stones_treated = number_of_stones_treated
       self.stone_burden=stone_burden



class ProcedureDetailsSchema(ma.Schema):
    class Meta:
        fields =('id','laser_system_serial_number','case_number','procedure_date','ecm_logs','surgical_videos','endoscopic_used','laser_source_information','light_source_lamp_age','imaging_mode','treatment_location','treatment_type','fiber_used','number_of_stones_treated','stone_burden')

procedureSchema = ProcedureDetailsSchema()
procedureSchemas = ProcedureDetailsSchema(many=True)


#Add new procedure

@app.route('/procedure', methods=['POST'])
def add_procedure():

    laser_system_serial_number = request.json['laser_system_serial_number']
    case_number = request.json['case_number']
    # procedure_date = datetime.datetime.now()
    procedure_date = request.json["procedure_date"]
    ecm_logs =request.json['ecm_logs']
    surgical_videos = request.json['surgical_videos']
    endoscopic_used = request.json['endoscopic_used']
    laser_source_information = request.json['laser_source_information']
    light_source_lamp_age = request.json['light_source_lamp_age']
    imaging_mode = request.json['imaging_mode']
    treatment_location = request.json['treatment_location']
    treatment_type = request.json['treatment_type']
    fiber_used = request.json['fiber_used']
    number_of_stones_treated = request.json['number_of_stones_treated']
    stone_burden = request.json['stone_burden']
    new_procedure = ProcedureDetails(
        laser_system_serial_number,case_number,procedure_date,ecm_logs,surgical_videos,
        endoscopic_used,laser_source_information,light_source_lamp_age,imaging_mode,treatment_location,
        treatment_type,fiber_used,number_of_stones_treated,stone_burden
    )
    db.session.add(new_procedure)
    db.session.commit()

    print(new_procedure)

    # return jsonify({'message': 'Procedure added successfully'}), 201
    return procedureSchema.jsonify(new_procedure), 201

#Get All Procedure Details
@app.route('/procedure',methods=['GET'])
# @swag_from('procedure.yml')  # Reference a YAML file for detailed docstring
def getAllProcedureDetails():
    all_procedurs = ProcedureDetails.query.all()
    result = procedureSchemas.dump(all_procedurs)
    return jsonify(result)


#Get Single Procedure Details By ID
@app.route('/procedure/<id>',methods=['GET'])
def getProcedureDetailByID(id):
    procedure = ProcedureDetails.query.get(id)
    return procedureSchema.jsonify(procedure)


#Update Single Procedure Details By ID
@app.route('/procedure/<id>',methods=['PUT'])
def updateProcedureDetailByID(id):
    procedure = ProcedureDetails.query.get(id)

    if 'treatment_location' in request.json:
        procedure.treatment_location = request.json['treatment_location']

    if 'number_of_stones_treated' in request.json:
        procedure.number_of_stones_treated = request.json['number_of_stones_treated']
    db.session.commit()

    return procedureSchema.jsonify(procedure)

#Delete Single Procedure Details By ID
@app.route('/procedure/<id>',methods=['DELETE'])
def deleteProcedureDetailByID(id):
    procedure = ProcedureDetails.query.get(id)
    db.session.delete(procedure)
    db.session.commit()
    return jsonify({'Status':'OK'}), 200



if __name__ == '__main__':
    app.run(debug=True, port=5000)
