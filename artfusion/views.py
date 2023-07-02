from flask import Blueprint, render_template, request, session, flash, url_for, redirect
from .models import Order, Artwork ,Artist
from datetime import datetime
from .forms import CheckoutForm
from . import db
import random

bp = Blueprint('main',__name__)

@bp.route('/')
def index(): 
    artist = Artist.query.filter(Artist.id).all()
    water_artworks = Artwork.query.filter(Artwork.artworkPaint.like('%Watercolor%')).order_by(Artwork.id).all()
    acrylic_artworks = Artwork.query.filter(Artwork.artworkPaint.like('%Acrylic%')).order_by(Artwork.id).all()
    w_artworks = random.sample(water_artworks, 3)
    a_artworks = random.sample(acrylic_artworks, 6)
    return render_template('index.html', artist = artist, water_artworks = w_artworks, acrylic_artworks = a_artworks )

@bp.route('/about-us/')
def aboutus():
    return render_template('aboutus.html')

@bp.route('/check-out/', methods=['POST', 'GET'])
def checkout():
    form = CheckoutForm() 
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
       
        if form.validate_on_submit():
            order.orderStatus = True
            order.fname = form.firstname.data
            order.lname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            totalcost = 0
            for artwork in order.artworks:
                totalcost = totalcost + artwork.price
            order.price = totalcost
            order.orderDate = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thanks for your request. Our team will get back to you as soon as possible.')
                return redirect(url_for('main.index'))
            except:
                flash ('Oops! There was an issue with your order!')
                return redirect(url_for('main.index'))
            
    f_artwork = Artwork.query.filter(Artwork.id).all()
    showartworks = random.sample(f_artwork, 3)    
    return render_template('checkout.html', form = form, f_artwork = showartworks)

@bp.route('/contactus/', methods=['POST', 'GET'])
def contactus():

    print('First Name: {}\nLast Name: {}\nEmail: {}\nOrder Number: {}\nAdditional Comments: {}'.format(
        request.form.get('firstname'),request.form.get('lastname'),request.form.get('email'),request.form.get('orderNumber'),request.form.get('textArea')))

    return render_template('contactus.html') 

@bp.route('/basket/', methods=['POST', 'GET'])
def basket():

    artwork_id = request.values.get('artwork_id')

    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])
    else:
        order = None

    if order is None:
        order = Order(fname = '', lname = '', email = '', phone = '', orderStatus = False, orderDate = datetime.now(), price = 0, discountCode = '')
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('New order was no able to be created')
            order = None
    
    totalprice = 0
    if order is not None:
        for artwork in order.artworks:
            totalprice = totalprice + artwork.price
    

    if artwork_id is not None and order is not None:
        artwork = Artwork.query.get(artwork_id)
        if artwork not in order.artworks:
            try:
                order.artworks.append(artwork)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.basket'))
        else:
            flash('item already in basket')
            return redirect(url_for('main.basket'))
        
    f_artwork = Artwork.query.filter(Artwork.id).all()
    showartworks = random.sample(f_artwork, 3)    
    return render_template('item-basket.html', order = order, totalprice = totalprice, f_artwork = showartworks)


@bp.route('/product-page/<int:artworkid>/')
def productpage(artworkid):
    artwork_details = Artwork.query.filter(Artwork.id == artworkid)
    featured_art = Artwork.query.filter(Artwork.review >= 5).order_by(Artwork.id).all()
    f_artworks = random.sample(featured_art, 3)
    return render_template('product-page.html' , artwork_details = artwork_details, featured_art = f_artworks)

@bp.route('/filtered/<int:artid>/')
def filtered(artid):
    artwork = Artwork.query.filter(Artwork.artist_id == artid)    
    return render_template('filtered-view.html', artwork = artwork)

# Delete specific basket items
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        artwork_to_delete = Artwork.query.get(id)
        try:
            order.artworks.remove(artwork_to_delete)
            db.session.commit()
            return redirect(url_for('main.basket'))
        except:
            return 'There was a problem deleting your item!'
    return redirect(url_for('main.basket'))


# Scrap basket
@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All Items Have Been Removed')
    return redirect(url_for('main.index'))