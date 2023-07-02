# imnport flask - from the package import a module
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


#Create new web application
# This will be run on a web server locally.
db = SQLAlchemy()
app=Flask(__name__) # package name

def create_app():
    app.debug=True
    app.secret_key='9w7QP5ey7TvamYPa'
    
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///artfusion.sqlite'

    db.init_app(app)

    bootstrap = Bootstrap(app)

    # New blueprint
    from . import views
    app.register_blueprint(views.bp)
    #from . import admin
    #app.register_blueprint(admin.bp)

    return app

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html')
