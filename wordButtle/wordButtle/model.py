from . import db

class rus (db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    word = db.Column(db.String(30))
    eng = db.Column(db.String(30))
    heb = db.Column(db.String(30))
    ger = db.Column(db.String(30))
    
    def __repr__(self):
        return '<rusкак %r>' % self.word

    @property
    def serialize(self):
        return {
                'id' : self.id,
                'word' : self.word,
                'eng' : self.eng,
                'heb' : self.heb,
                'ger' : self.ger
            }

class User(db.Model):
     id = db.Column(db.Integer, primary_key=True, unique = True)
     Name = db.Column(db.String(1000), unique=True)
     DeviceID = db.Column(db.String(1000), unique=True)

     def __repr__(self):
        return '<User %r>' % self.id

     @property
     def serialize(self):
        return {
                'id' : self.id,
                'Name' : self.Name,
                'DeviceID' : self.DeviceID
            }

class Rooms(db.Model):
     id = db.Column(db.Integer, primary_key=True, unique = True)
     Name = db.Column(db.String(1000))
     CreatorName = db.Column(db.String(1000))
     ConnectorName = db.Column(db.String(1000))
     isShown = db.Column(db.Integer)

     def __repr__(self):
        return '<Rooms %r>' % self.id

     @property
     def serialize(self):
        return {
                "id" : self.id,
                "Name" : self.Name,
                "CreatorName" : self.CreatorName,
                "ConnectorName" : self.ConnectorName,
                "isShown" : self.isShown
            }

class rusltab (db.Model):
    id = db.Column(db.String(10), primary_key=True, unique=True)
    l1 = db.Column(db.Integer)
    l2 = db.Column(db.Integer)
    l3 = db.Column(db.Integer)
    l4 = db.Column(db.Integer)
    l5 = db.Column(db.Integer)
    l6 = db.Column(db.Integer)
    l7 = db.Column(db.Integer)
    l8 = db.Column(db.Integer)
    l9 = db.Column(db.Integer)
    l10 = db.Column(db.Integer)
    l11 = db.Column(db.Integer)
    l12 = db.Column(db.Integer)
    l13 = db.Column(db.Integer)
    l14 = db.Column(db.Integer)
    l15 = db.Column(db.Integer)
    l16 = db.Column(db.Integer)
    l17 = db.Column(db.Integer)
    l18 = db.Column(db.Integer)
    l19 = db.Column(db.Integer)
    l20 = db.Column(db.Integer)
    l21 = db.Column(db.Integer)
    l22 = db.Column(db.Integer)
    l23 = db.Column(db.Integer)
    l24 = db.Column(db.Integer)
    l25 = db.Column(db.Integer)
    l26 = db.Column(db.Integer)
    l27 = db.Column(db.Integer)
    l28 = db.Column(db.Integer)
    l29 = db.Column(db.Integer)
    l30 = db.Column(db.Integer)
    l31 = db.Column(db.Integer)
    l32 = db.Column(db.Integer)

    def __repr__(self):
        return '<rusLTab %r>' % self.id

    @property
    def serialize(self):
       return {
                'id' : self.id,
                'l1' : self.l1,
                'l2' : self.l2,
                'l3' : self.l3,
                'l4' : self.l4,
                'l5' : self.l5,
                'l6' : self.l6,
                'l7' : self.l7,
                'l8' : self.l8,
                'l9' : self.l9,
                'l10' : self.l10,
                'l11' : self.l11,
                'l12' : self.l12,
                'l13' : self.l13,
                'l14' : self.l14,
                'l15' : self.l15,
                'l16' : self.l16,
                'l17' : self.l17,
                'l18' : self.l18,
                'l19' : self.l19,
                'l20' : self.l20,
                'l21' : self.l21,
                'l22' : self.l22,
                'l23' : self.l23,
                'l24' : self.l24,
                'l25' : self.l25,
                'l26' : self.l26,
                'l27' : self.l27,
                'l28' : self.l28,
                'l29' : self.l29,
                'l30' : self.l30,
                'l31' : self.l31,
                'l32' : self.l32
            }