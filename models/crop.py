from server_config import db

class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), nullable=False)
    variation = db.Column(db.String(80), nullable=False)
    num_seeds = db.Column(db.Integer, nullable=False)
    supervisor = db.Column(db.String(80), nullable=False)

    plot_id = db.Column(db.Integer, db.ForeignKey('plot.id'), nullable=False)
    plot = db.relationship('Plot', backref=db.backref('crop', lazy=True), uselist=False)

    def to_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'variation': self.variation,
            'num_seeds': self.num_seeds,
            'supervisor': self.supervisor,
            'plot_id': self.plot_id
        }

    def __repr__(self):
        return f'<Crop {self.id}>'

    def insert(type, variation, num_seeds, supervisor, plot_id):
        crop = Crop(
            type=type,
            variation=variation,
            num_seeds=num_seeds,
            supervisor=supervisor,
            plot_id=plot_id
        )

        db.session.add(crop)
        db.session.commit()
        return crop

    def get_all():
        return Crop.query.all()