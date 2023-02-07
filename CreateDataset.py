import os

import cv2
import numpy as np
from tqdm import tqdm

IMG_SIZE = (50, 50)


class VarroavsNoVarroa():
    SI_VARROA = "SiVarroa"
    NO_VARROA = "NoVarroa2"
    LABELS = {NO_VARROA: 0, SI_VARROA: 1}
    si_varroa_count = 0
    no_varroa_count = 0
    training_data = []

    def make_training_data(self):
        print("Preparando i dati...\n")
        for label in self.LABELS:
            for f in tqdm(os.listdir(label)):
                try:
                    path = os.path.join(label, f)
                    img = cv2.imread(path)
                    bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                    resized = cv2.resize(bgr, IMG_SIZE)
                    self.training_data.append([resized, np.eye(2)[self.LABELS[label]]])

                    if label == self.SI_VARROA:
                        self.si_varroa_count += 1
                    elif label == self.NO_VARROA:
                        self.no_varroa_count += 1
                except Exception as e:
                    pass
        np.random.shuffle(self.training_data)
        np.save("training_data.npy", self.training_data)
        print("Varroa: ", self.si_varroa_count)
        print("No Varroa:", self.no_varroa_count)


if __name__ == "__main__":
    sv_vs_nv = VarroavsNoVarroa()
    sv_vs_nv.make_training_data()
