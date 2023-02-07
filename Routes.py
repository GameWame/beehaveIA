from flask import render_template, Blueprint

views = Blueprint('views', __name__)


@views.route('/')
@views.route('/default')
def home():
    return render_template('inserisci_ape.html')
