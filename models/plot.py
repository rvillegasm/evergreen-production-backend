from server_config import db

class Plot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    state = db.Column(db.String(80), nullable=False)
    available = db.Column(db.Boolean, nullable=False)
    num_workers = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Plot {self.id}>'
  
  