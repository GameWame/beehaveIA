from BeeClassifier import BeeClassifier


class AdapterVarroa(BeeClassifier):
    def __init__(self, model):
        self.model = model

    def classify(self, image):
        return self.model.predict(image)
