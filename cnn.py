import numpy as np
import torch
from tqdm import tqdm

from Net import Net

"""Acquisizione Dataset"""
data = np.load("training_data.npy", allow_pickle=True)

"""Rete Neurale"""
net = Net()

"""Ottimizzatore della rete"""
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)

"""Funzione di perdita"""
loss_function = torch.nn.MSELoss()

"""Dati"""
X = torch.Tensor(np.array([i[0] for i in data])).view(-1, 50, 50)

"""Feature Scaling"""
X = X / 255.0

"""Etichette"""
Y = torch.Tensor(np.array([i[1] for i in data]))

"""Percentuale divisione training e test set"""
VAL_PCT = 0.3
val_size = int(len(X) * VAL_PCT)
print("Val size: {}\n".format(val_size))

"""Training set"""
train_X = X[:-val_size]
train_Y = Y[:-val_size]

"""Test set"""
test_X = X[-val_size:]
test_Y = Y[-val_size:]

"""Numero passi"""
BATCH_SIZE = 3

"""Numero Iterazioni rete"""
EPOCHS = 3

print("Training iniziato...\n")

for epoch in range(EPOCHS):
    for i in tqdm(range(0, len(train_X), BATCH_SIZE)):
        batch_X = train_X[i:i + BATCH_SIZE].view(-1, 1, 50, 50)
        batch_Y = train_Y[i:i + BATCH_SIZE]
        net.zero_grad()

        outputs = net(batch_X)
        loss = loss_function(outputs, batch_Y)
        loss.backward()
        optimizer.step()
correct = 0
total = 0

"""Calcolo metriche di valutazione"""

"""Accuracy"""
with torch.no_grad():
    for i in tqdm(range(len(test_X))):
        real_class = torch.argmax(test_Y[i])
        net_out = net(test_X[i].view(-1, 1, 50, 50))[0]
        predicted_class = torch.argmax(net_out)
        if predicted_class == real_class:
            correct += 1
        total += 1
print("Accuracy : {}".format(correct / total))

"""Precision"""
with torch.no_grad():
    for i in tqdm(range(len(test_X))):
        real_class = torch.argmax(test_Y[i])
        net_out = net(test_X[i].view(-1, 1, 50, 50))[0]
        predicted_class = torch.argmax(net_out)
        if predicted_class == real_class and real_class == 1:
            correct += 1
        total += 1
print("Precision : {}".format(correct / total))

"""Recall"""
with torch.no_grad():
    for i in tqdm(range(len(test_X))):
        real_class = torch.argmax(test_Y[i])
        net_out = net(test_X[i].view(-1, 1, 50, 50))[0]
        predicted_class = torch.argmax(net_out)
        if predicted_class == real_class and real_class == 0:
            correct += 1
        total += 1
print("Recall : {}".format(correct / total))