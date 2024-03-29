import numpy as np
import torch
import TestNet
from tqdm import tqdm

from CreateDataset import IMG_SIZE
from Net import Net


def train():
    """Acquisizione Dataset"""
    data = np.load("training_data.npy", allow_pickle=True)

    """Rete Neurale"""
    net = Net()

    """Ottimizzatore della rete"""
    optimizer = torch.optim.Adam(net.parameters(), lr=0.001)

    """Funzione di perdita"""
    loss_function = torch.nn.L1Loss()

    """Dati"""
    X = torch.Tensor(np.array([i[0] for i in data])).view(-1, IMG_SIZE[0], IMG_SIZE[1], 3)

    """Feature Scaling"""
    X = X / 255.0

    """Etichette"""
    Y = torch.Tensor(np.array([i[1] for i in data]))

    """Percentuale divisione training e test set"""
    VAL_PCT = 0.1
    val_size = int(len(X) * VAL_PCT)
    print("Val size: {}\n".format(val_size))

    """Training set"""
    train_X = X[:-val_size]
    train_Y = Y[:-val_size]

    """Test set"""
    test_X = X[-val_size:]
    test_Y = Y[-val_size:]

    """Numero passi"""
    BATCH_SIZE = 50

    """Numero Iterazioni rete"""
    EPOCHS = 4

    print("Training iniziato...\n")

    for epoch in range(EPOCHS):
        for i in tqdm(range(0, len(train_X), BATCH_SIZE)):
            batch_X = train_X[i:i + BATCH_SIZE].view(-1, 3, IMG_SIZE[0], IMG_SIZE[1])
            batch_Y = train_Y[i:i + BATCH_SIZE]
            net.zero_grad()

            outputs = net(batch_X)
            loss = loss_function(outputs, batch_Y)
            loss.backward()
            optimizer.step()

    """Calcolo metriche di valutazione"""
    metrics = TestNet.test(test_X, test_Y, net)
    print("Accuracy: {}\n".format(metrics["accuracy"]))
    print("Precision: {}\n".format(metrics["precision"]))
    print("Recall: {}\n".format(metrics["recall"]))

    torch.save(net.state_dict(), "VarroaModel.pth")

    return net


if __name__ == "__main__":
    train()
