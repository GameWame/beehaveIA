from flask import request, Blueprint, flash
import os

from AdapterVarroa import AdapterVarroa
from Routes import default_page
from BeeClassifier import BeeClassifier

ALLOWED_EXTENSIONS = {'jpeg'}

gia = Blueprint("gia", __name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@gia.route('/inserisci_img_ape', methods=['GET', 'POST'])
def inserisci_img_ape():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            print('No file found.')
            return default_page()

        if file == '':
            print('No selected file.')
            return default_page()

        file.save(file.filename)
        classifier = BeeClassifier()
        adapter = AdapterVarroa(classifier)
        if adapter.classify(file.filename):
            flash("Ape affetta dal parassita Varroa Destructor")
        else:
            flash("Ape non affetta da nessun parassita")
        print("File Uploaded.")
        os.remove(file.filename)

    return default_page()
