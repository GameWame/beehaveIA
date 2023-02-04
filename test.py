import numpy as np
from matplotlib import pyplot
training_data = np.load("training_data.npy", allow_pickle=True)

for i in range(0, 10):
    pyplot.imshow(training_data[i][0])
    print(training_data[i])
    pyplot.show()
