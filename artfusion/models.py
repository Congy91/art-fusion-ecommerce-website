from . import db

class Artist(db.Model):
    __tablename__='artists'
    id= db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    location = db.Column(db.String(80), nullable=True)
    numberOfPaintings = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String(60), nullable=False, default='template_img.jpg')
    artworks = db.relationship('Artwork', backref='Artist', cascade="all, delete-orphan")

    def __repr__(self):
        str = "ID: {}\nName: {} {}\nAge: {}\nLocation: {}\nNumber Of Paintings: {}\n"
        str = str.format(self.id, self.fname, self.lname, self.age, self.location, self.numberOfPaintings)
        return str
    
orderdetails = db.Table('orderdetails',
    db.Column('order_id',db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('artwork_id',db.Integer,db.ForeignKey('artworks.id'), nullable=False),
    db.PrimaryKeyConstraint('order_id', 'artwork_id'))
    
class Artwork(db.Model):
    __tablename__='artworks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False, default='template_img.jpg')
    price = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Integer, nullable=False)
    inStock = db.Column(db.Boolean, default=True)
    artworkSize = db.Column(db.String(32), nullable=False)
    artworkStyle = db.Column(db.String(60), nullable=False)
    artworkPaint = db.Column(db.String(60), nullable=False)
    artworkDate = db.Column(db.DateTime, nullable=False)
    artistName = db.Column(db.String(60), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

    def __repr__(self):
        str = "ID: {}\nName: {}\nDescription: {}\nImage: {}\nPrice: {}\nReview: {}\nIn Stock: {}\nArtist: {}\nArtwork Size: {}\nArtwork Style: {}\nArtwork Paint: {}\nArtwork Date: {}"
        str = str.format(self.id, self.name, self.description, self.image, self.price, self.review, self.inStock, self.artist_id, self.artworkSize, self.artworkStyle, self.artworkPaint, self.artworkDate)
        return str
    
class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(64))
    lname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    orderStatus = db.Column(db.Boolean, default=False)
    orderDate = db.Column(db.DateTime)
    price = db.Column(db.Integer)
    discountCode = db.Column(db.String(32))
    artworks = db.relationship('Artwork', secondary=orderdetails, backref='orders')

    def __repr__(self):
        str = "Order Number: {}\nName: {} {}\nEmail: {}\nPhone: {}\nOrder Status: {}\nOrder Date: {}\nPrice: {}\nArtwork: {}\nUser: {}\n,Discount Code: {}\n"
        str = str.format(self.id, self.fname, self.lname, self.email, self.phone, self.orderStatus, self.orderDate, self.price, self.artwork_id, self.discountCode)
        return str
    
class Review(db.Model):
    __tablename__='reviews'
    id = db.Column(db.Integer, primary_key=True)
    starRating = db.Column(db.Integer, nullable=False)
    reviewText = db.Column(db.String(500), nullable=False)
    user = db.Column(db.String(64))
    #artwork_id = db.relationship('Artwork', secondary=orderdetails, backref='reviews')

    def __repr__(self):
        str = "ID: {}\nStar Rating: {}\nReview Text: {}\nUser: {}\nProduct: {}\n"
        str = str.format(self.id, self.starRating, self.reviewText, self.user, self.artwork_id)
        return str
    
class Support(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    ticketStatus = db.Column(db.Boolean, default=False)
    user = db.Column(db.String(64))
    issueRequest = db.Column(db.String(500), nullable=False)
    issueType = db.Column(db.String(64))

    def __repr__(self):
        str = "ID: {}\nTicket Status: {}\nUser: {}\nIssue Request: {}\nIssue Type: {}\n"
        str = str.format(self.id, self.ticketStatus, self.user, self.issueRequest, self.issueType)
        return str
    