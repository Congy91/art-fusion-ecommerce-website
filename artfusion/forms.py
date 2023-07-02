from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, SelectField, IntegerField
from wtforms.validators import InputRequired, Email

# Form used for checkout

class CheckoutForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    address = StringField('Address', validators=[InputRequired()])
    city = StringField('City', validators=[InputRequired()])
    postal_code = StringField('Postal Code', validators=[InputRequired()])
    country = SelectField('Country', validators=[InputRequired()], choices=[
        ('', 'Select Country'),
        ('AU', 'Australia'),
        ('US', 'United States'),
        ('AF', 'Africa'),       

    ])
    payment_method = SelectField('Payment Method', validators=[InputRequired()], choices=[
        ('', 'Select Payment Method'),
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
    ])
    card_number = StringField('Card Number', validators=[InputRequired()])
    card_cvv = IntegerField('CVV', validators=[InputRequired()])
    card_expiry_month = IntegerField('Expiry Month', validators=[InputRequired()])
    card_expiry_year = IntegerField('Expiry Year', validators=[InputRequired()])
    submit = SubmitField('Place Order')


   
