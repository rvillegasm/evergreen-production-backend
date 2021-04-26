from server_config import db

class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), nullable=False)
    variation = db.Column(db.String(80), nullable=False)
    num_seeds = db.Column(db.Integer, nullable=False)
    supervisor = db.Column(db.String(80), nullable=False)

    plot_id = db.Column(db.Integer, db.ForeignKey('plot.id'), nullable=False)
    plot = db.relationship('Plot', backref=db.backref('crop', lazy=True), uselist=False)

    def __repr__(self):
        return f'<Crop {self.id}>'