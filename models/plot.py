from server_config import db

class Plot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    state = db.Column(db.String(80), nullable=False)
    available = db.Column(db.Boolean, nullable=False)
    num_workers = db.Column(db.Integer, nullable=False)

    def mark_as_used(self):
        self.available = False
        db.session.commit()

    def to_json(self):
        return {
            'id': self.id,
            'area': self.area,
            'lat': self.lat,
            'lng': self.lng,
            'state': self.state,
            'available': self.available,
            'num_workers': self.num_workers
        }

    def __repr__(self):
        return f'<Plot {self.id}>'
  
    def insert(area, lat, lng, state, available, num_workers):
        plot = Plot(
            area=area,
            lat=lat,
            lng=lng,
            state=state,
            available=available,
            num_workers=num_workers
        )

        db.session.add(plot)
        db.session.commit()
        return plot

    def get_all():
        return Plot.query.all()

    def get_by_id(id):
        return Plot.query.filter_by(id=str(id)).first()