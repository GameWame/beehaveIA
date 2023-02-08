from flask import render_template, Blueprint

views = Blueprint("views", __name__)


@views.route('/')
@views.route('/default_page')
def default_page():
    return render_template('inserisci_ape.html')
