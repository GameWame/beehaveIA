from flask import flash

from BeeClassifier import BeeClassifier


class AdapterVarroa(BeeClassifier):
    def __init__(self, model):
        self.model = model

    def classify(self, image):
        if self.model.predict(image):
            flash("Ape affetta dal parassita Varroa Destructor")
        else:
            flash("Ape non affetta da nessun parassita")