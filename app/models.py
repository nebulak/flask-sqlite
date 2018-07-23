from app import db

class Point(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __init__(self, title, description, lat, lon):
        self.title = title
        self.description = description
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return '<User %r>' % self.title
