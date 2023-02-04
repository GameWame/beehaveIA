import torch
from tqdm import tqdm

"""Accuracy"""


def accuracy(test_X, test_Y, net):
    total = 0
    correct = 0
    with torch.no_grad():
        for i in tqdm(range(len(test_X))):
            real_class = torch.argmax(test_Y[i])
            net_out = net(test_X[i].view(-1, 1, 50, 50))[0]
            predicted_class = torch.argmax(net_out)
            if predicted_class == real_class:
                correct += 1
            total += 1
    return correct / total


"""Precision"""


def precision(test_X, test_Y, net):
    total = 0
    correct = 0
    with torch.no_grad():
        for i in tqdm(range(len(test_X))):
            real_class = torch.argmax(test_Y[i])
            net_out = net(test_X[i].view(-1, 1, 50, 50))[0]
            print(net_out)
            predicted_class = torch.argmax(net_out)
            if int(predicted_class):
                if predicted_class == real_class:
                    correct += 1
                total += 1
    return correct / total


"""Recall"""


def recall(test_X, test_Y, net):
    total = 0
    correct = 0
    with torch.no_grad():
        for i in tqdm(range(len(test_X))):
            real_class = torch.argmax(test_Y[i])
            net_out = net(test_X[i].view(-1, 1, 50, 50))[0]
            predicted_class = torch.argmax(net_out)
            if int(real_class):
                if predicted_class == real_class:
                    correct += 1
            total += 1
    return correct / total
