
from flask import Blueprint
from . import db
from .models import Artist, Artwork, Order
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    artist1 = Artist(fname='Isabella', lname='Nguyen', age=32, location='Sydney', numberOfPaintings=2,image = 'artist3.jpg')
    artist2 = Artist(fname='Liam', lname='Chen', age=28, location='Melbourne', numberOfPaintings=3, image='artist1.jpg')
    artist3 = Artist(fname='Ava', lname='Tran', age=35, location='Brisbane', numberOfPaintings=4, image='artist4.jpg')
    artist4 = Artist(fname='Noah', lname='Gupta', age=31, location='Perth', numberOfPaintings=3, image ='artist2.jpg' )
    artist5 = Artist(fname='Mia', lname='Singh', age=29, location='Adelaide', numberOfPaintings=2, image ='artist5.jpg' )
    artist6 = Artist(fname='William', lname='Kim', age=33, location='Darwin', numberOfPaintings=4, image ='artist6.jpg' )
      
    try:
        db.session.add(artist1)
        db.session.add(artist2)
        db.session.add(artist3)
        db.session.add(artist4)
        db.session.add(artist5)
        db.session.add(artist6)
        db.session.commit()
    except:
        return 'There was an issue adding the "ARTISTS" in dbseed function'

    
    artwork1 = Artwork(name='African Serenity', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='o_painting1.jpg', price=250, review=3, inStock = True, artworkSize='16x20 inches', artworkStyle='Impressionism', artworkPaint='Oil', artworkDate=datetime.datetime(2022, 4, 15),artistName=artist1.fname, artist_id=artist1.id)
    artwork2 = Artwork(name='Intrigue', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='a_painting1.jpg', price=180, review=4, inStock = True,artworkSize='12x12 inches', artworkStyle='Abstract', artworkPaint='Acrylic', artworkDate=datetime.datetime(2021, 9, 5),artistName=artist1.fname, artist_id=artist1.id)

    artwork3 = Artwork(name='Rainy Day', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='w_painting1.jpg', price=150, review=5, inStock = True,artworkSize='18x24 inches', artworkStyle='Contemporary', artworkPaint='Watercolor', artworkDate=datetime.datetime(2023, 1, 12),artistName=artist2.fname, artist_id=artist2.id)
    artwork4 = Artwork(name='Beauty From Ashes', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='r_painting1.jpg', price=200, review=4, inStock = True,artworkSize='20x20 inches', artworkStyle='Abstract', artworkPaint='Mixed Media', artworkDate=datetime.datetime(2022, 7, 20),artistName=artist2.fname, artist_id=artist2.id)
    artwork5 = Artwork(name='Wisdoms Glory', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='o_painting2.jpg', price=220, review=5, inStock = True,artworkSize='16x20 inches', artworkStyle='Realism', artworkPaint='Oil', artworkDate=datetime.datetime(2022, 2, 8),artistName=artist2.fname, artist_id=artist2.id)

    artwork6 = Artwork(name='Mystic Forest', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='a_painting2.jpg', price=280, review=5, inStock = True,artworkSize='24x36 inches', artworkStyle='Fantasy', artworkPaint='Acrylic', artworkDate=datetime.datetime(2021, 12, 2),artistName=artist3.fname, artist_id=artist3.id)
    artwork7 = Artwork(name='Ancient Wonderings', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='o_painting3.jpg', price=300, review=3, inStock = True,artworkSize='24x30 inches', artworkStyle='Impressionism', artworkPaint='Oil', artworkDate=datetime.datetime(2022, 6, 17),artistName=artist3.fname, artist_id=artist3.id)
    artwork8 = Artwork(name='Frozen River', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='r_painting2.jpg', price=220, review=4, inStock = True,artworkSize='16x20 inches', artworkStyle='Abstract', artworkPaint='Mixed Media', artworkDate=datetime.datetime(2022, 3, 4),artistName=artist3.fname, artist_id=artist3.id)
    artwork9 = Artwork(name='Busy Life', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='w_painting2.jpg', price=250, review=5, inStock = True,artworkSize='18x24 inches', artworkStyle='Realism', artworkPaint='Watercolor', artworkDate=datetime.datetime(2021, 8, 22),artistName=artist3.fname, artist_id=artist3.id)
   
    artwork10 = Artwork(name='Evening Gathering', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='o_painting4.jpg', price=180, review=4, inStock = True,artworkSize='14x18 inches', artworkStyle='Impressionism', artworkPaint='Oil', artworkDate=datetime.datetime(2022, 9, 10),artistName=artist4.fname, artist_id=artist4.id)
    artwork11 = Artwork(name='House On A Boat', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='a_painting3.jpg', price=200, review=5, inStock = True,artworkSize='16x20 inches', artworkStyle='Contemporary', artworkPaint='Acrylic', artworkDate=datetime.datetime(2022, 5, 3),artistName=artist4.fname, artist_id=artist4.id)
    artwork12 = Artwork(name='Date Night', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='w_painting3.jpg', price=220, review=5, inStock = True,artworkSize='18x24 inches', artworkStyle='Realism', artworkPaint='Watercolor', artworkDate=datetime.datetime(2022, 1, 18),artistName=artist4.fname, artist_id=artist4.id)
   
    artwork13 = Artwork(name='Spirit of Nature', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='r_painting3.jpg', price=280, review=4, inStock = True,artworkSize='20x30 inches', artworkStyle='Realism', artworkPaint='Oil on canvas', artworkDate=datetime.datetime(2022, 2, 8),artistName=artist5.fname, artist_id=artist5.id)
    artwork14 = Artwork(name='Dark Forest', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='a_painting4.jpg', price=320, review=3, inStock = True,artworkSize='24x36 inches', artworkStyle='Landscape', artworkPaint='Acrylic on canvas', artworkDate=datetime.datetime(2022, 7, 14),artistName=artist5.fname, artist_id=artist5.id)
   
    artwork15 = Artwork(name='Imagination', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='a_painting6.jpg', price=380, review=4, inStock = True, artworkSize='24x24 inches', artworkStyle='Surrealism', artworkPaint='Mixed media', artworkDate=datetime.datetime(2023, 3, 10),artistName=artist6.fname, artist_id=artist6.id)
    artwork16 = Artwork(name='Vibrant Splash', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='a_painting5.jpg', price=200, review=4, inStock = True,artworkSize='16x20 inches', artworkStyle='Abstract', artworkPaint='Acrylic on canvas', artworkDate=datetime.datetime(2023, 5, 22),artistName=artist6.fname, artist_id=artist6.id)
    artwork17 = Artwork(name='Urban Village', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='r_painting4.jpg', price=320, review=5, inStock = True,artworkSize='24x36 inches', artworkStyle='Realism', artworkPaint='Oil on canvas', artworkDate=datetime.datetime(2023, 6, 5),artistName=artist6.fname, artist_id=artist6.id)
    artwork18 = Artwork(name='Street Life', description='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut vitae dolorum eum, eligendi vero dolore a ea unde totam culpa veniam itaque assumenda repellat quibusdam voluptas! Debitis odio sapiente ea! Exercitationem incidunt mollitia quidem delectus! Ad nisi aperiam corporis.', image='r_painting5.jpg', price=280, review=5, inStock = True,artworkSize='18x24 inches', artworkStyle='Expressionism', artworkPaint='Acrylic on canvas', artworkDate=datetime.datetime(2023, 4, 19),artistName=artist6.fname, artist_id=artist6.id)


    try:
        db.session.add(artwork1)
        db.session.add(artwork2)
        db.session.add(artwork3)
        db.session.add(artwork4)
        db.session.add(artwork5)
        db.session.add(artwork6)
        db.session.add(artwork7)
        db.session.add(artwork8)
        db.session.add(artwork9)
        db.session.add(artwork10)
        db.session.add(artwork11)
        db.session.add(artwork12)
        db.session.add(artwork13)
        db.session.add(artwork14)
        db.session.add(artwork15)
        db.session.add(artwork16)
        db.session.add(artwork17)
        db.session.add(artwork18)
        db.session.commit()
    except:
        return 'There was an issue adding a "ARTWORK" in dbseed function'

    return 'DATA LOADED'


