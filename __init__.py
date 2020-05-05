import os

from flask import Flask, render_template

def create_app(test_config=None):
    # create and configfure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'sheets.sqlite'),
    )

    if test_config is None:
        # load the instanfce config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #@app.route("/")
    #def hello_world():
    #    return render_template("home.html.j2")

    #@app.route("/user/<username>")
    #def user_profile(username):
    #    return "User %s" % escape(username)

    #@app.route("/login",methods=["GET","POST"])
    #def login():
    #    return render_template("home.html.j2")

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)


    return app

