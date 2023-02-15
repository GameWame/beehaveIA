from flask import flash

from BeeClassifier import BeeClassifier


class AdapterVarroa(BeeClassifier):

    def classify(self, image):
        if self.predict(image):
            flash("Ape affetta dal parassita Varroa Destructor")
        else:
            flash("Ape non affetta da nessun parassita")