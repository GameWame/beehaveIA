import matplotlib.pyplot as plt
from matplotlib import interactive

"""Valori testati di numero epoche e batch"""
epochs = ['1', '2', '3', '4', '5', '6', '7']
batches = ['10', '50', '100', '150', '200']

"""Risultati della media tra precision e recall riscontrati nel corrispondente numero di epoche o batch"""
ep_values = [0, 0.27, 0.63, 0.72, 0.67, 0.73, 0.75]
ba_values = [0.6, 0.67, 0.55, 0.3, 0]


plt.figure(figsize=(9, 3))
plt.suptitle('Media di valori per numero di epoche')
plt.plot(epochs, ep_values, "-oy")
plt.xlim(0, 7)
plt.ylim(0, 1)
interactive(True)
plt.show()

plt.figure(figsize=(9, 3))
plt.suptitle('Media di valori per numero di batch')
plt.plot(batches, ba_values, "-oy")
plt.ylim(0, 1)
interactive(False)
plt.show()
