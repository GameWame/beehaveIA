import cv2
import torch
from torch import Tensor

from CreateDataset import IMG_SIZE
from Net import Net

img = cv2.imread("SiVarroa/0CRzEsP2ONDJtOkqP8fSSE5Dif7iaVoB.jpeg")
resized = cv2.resize(img, IMG_SIZE)
resized = Tensor(resized).view(-1, IMG_SIZE[0], IMG_SIZE[1], 3)[0]

resized = resized / 255
net = Net()
load = torch.load("VarroaModelBest.pth")
net.load_state_dict(load)
net.eval()
with torch.no_grad():
    result = net(resized.view(-1,  3, IMG_SIZE[0], IMG_SIZE[1]))[0]
print(result)
if torch.argmax(result):
    print("SI Varroa")
else:
    print("No Varroa")
