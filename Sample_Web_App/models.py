from Sample_Web_App import db

#db = SQLAlchemy()

class VEHICLETBL(db.Model):
    __tablename__ = 'VEHICLE_TBL'

    VEHICLE_VIN = db.Column(db.String(30, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    VEHICLE_NAME = db.Column(db.String(30, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    VEHICLE_CITY = db.Column(db.String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    VEHICLE_STATUS = db.Column(db.String(20, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    VEHICLE_LASTUPDATE = db.Column(db.DateTime, nullable=False, server_default=db.text("(getdate())"))