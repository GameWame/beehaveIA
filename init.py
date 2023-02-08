from flask import Flask, render_template

"""Inizializzazione"""


def create_app():
    app = Flask(__name__)

    from Routes import views
    from inserimento_ape import gia

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(gia, url_prefix='/')

    @app.errorhandler(401)
    def unauthorized_user(e):
        # note that we set the 401 status explicitly
        return render_template('login_page.html'), 401

    @app.errorhandler(404)
    def page_not_found(e):
        # note that we set the 404 status explicitly
        return render_template('pageerror.html'), 404

    return app


app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
