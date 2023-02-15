from flask import request, Blueprint
import os

from AdapterVarroa import AdapterVarroa
from Routes import default_page
from BeeClassifier import BeeClassifier

gia = Blueprint("gia", __name__)


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
        adapter = AdapterVarroa()
        adapter.classify(file.filename)
        print("File Uploaded.")
        os.remove(file.filename)

    return default_page()
