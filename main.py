import cv2
import torch

from CreateDataset import IMG_SIZE
from Net import Net

img = cv2.imread("SiVarroa/0CRzEsP2ONDJtOkqP8fSSE5Dif7iaVoB.jpeg")
bgr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized = cv2.resize(bgr, IMG_SIZE)


net = Net()

net.load_state_dict(torch.load("VarroaModel.pth"))

result = net(resized)
print(result)
