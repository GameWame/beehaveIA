from flask import Flask

"""Inizializzazione"""


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'BEEHAVE'
    from Routes import views
    from inserimento_ape import gia

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(gia, url_prefix='/')

    return app


app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
