import torch
from tqdm import tqdm
from CreateDataset import IMG_SIZE
"""Accuracy"""


def accuracy(test_X, test_Y, net):
    net.eval()
    total = 0
    correct = 0
    with torch.no_grad():
        for i in tqdm(range(len(test_X))):
            real_class = torch.argmax(test_Y[i])
            net_out = net(test_X[i].view(-1, 3, IMG_SIZE[0], IMG_SIZE[1]))[0]
            predicted_class = torch.argmax(net_out)
            if predicted_class == real_class:
                correct += 1
            total += 1
    return correct / total


"""Precision"""


def precision(test_X, test_Y, net):
    net.eval()
    total = 0
    correct = 0
    with torch.no_grad():
        for i in tqdm(range(len(test_X))):
            real_class = torch.argmax(test_Y[i])
            net_out = net(test_X[i].view(-1, 3,  IMG_SIZE[0], IMG_SIZE[1]))[0]
            predicted_class = torch.argmax(net_out)
            if int(predicted_class):
                if predicted_class == real_class:
                    correct += 1
                total += 1
    if not total:
        return 0
    return correct / total


"""Recall"""


def recall(test_X, test_Y, net):
    net.eval()
    total = 0
    correct = 0
    with torch.no_grad():
        for i in tqdm(range(len(test_X))):
            real_class = torch.argmax(test_Y[i])
            net_out = net(test_X[i].view(-1, 3,  IMG_SIZE[0], IMG_SIZE[1]))[0]
            predicted_class = torch.argmax(net_out)
            if int(real_class):
                if predicted_class == real_class:
                    correct += 1
                total += 1
    if not total:
        return "No Positive in test set"
    return correct / total
