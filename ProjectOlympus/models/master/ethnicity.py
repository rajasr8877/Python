from db import db

class EthnicityModel(db.Model):
    __tablename__ = "ethnicity"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    isActive = db.Column(db.Boolean, default=True)
    created_At = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_At = db.Column(
        db.TIMESTAMP,
        server_default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )