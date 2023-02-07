import torch
from tqdm import tqdm
from CreateDataset import IMG_SIZE

"""Accuracy, Precision, Recall"""


def test(test_X, test_Y, net):
    net.eval()
    correct_accuracy = 0
    total_accuracy = 0
    correct_precision = 0
    total_precision = 0
    correct_recall = 0
    total_recall = 0

    parametervalues = {"accuracy": 0, "precision": 0, "recall": 0}
    with torch.no_grad():
        for i in tqdm(range(len(test_X))):
            real_class = torch.argmax(test_Y[i])
            net_out = net(test_X[i].view(-1, 3, IMG_SIZE[0], IMG_SIZE[1]))[0]
            predicted_class = torch.argmax(net_out)
            if predicted_class == real_class:
                correct_accuracy += 1
            total_accuracy += 1

            if int(predicted_class):
                if predicted_class == real_class:
                    correct_precision += 1
                total_precision += 1

            if int(real_class):
                if predicted_class == real_class:
                    correct_recall += 1
                total_recall += 1

        if total_accuracy:
            parametervalues["accuracy"] = correct_accuracy / total_accuracy
        if total_precision:
            parametervalues["precision"] = correct_precision / total_precision
        if total_recall:
            parametervalues["recall"] = correct_recall / total_recall

    return parametervalues
