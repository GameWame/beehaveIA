import cv2
import numpy as np
import torch
from torch import Tensor

from CreateDataset import IMG_SIZE
from Net import Net

img = cv2.imread("SiVarroa/0CRzEsP2ONDJtOkqP8fSSE5Dif7iaVoB.jpeg")
bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
resized = cv2.resize(bgr, IMG_SIZE)
resized = Tensor(np.array(resized))

resized = resized / 255
net = Net()
load = torch.load("VarroaModel.pth")
net.load_state_dict(load)
result = net(resized.view(-1, 3, IMG_SIZE[0], IMG_SIZE[0]))
print(result)
