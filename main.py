import cv2
import torch
from torch import Tensor

from CreateDataset import IMG_SIZE
from Net import Net
from cnn import train

#net = train()
#torch.save(net.state_dict(), "./VarroaModel.pth")

img = cv2.imread("SiVarroa/0CRzEsP2ONDJtOkqP8fSSE5Dif7iaVoB.jpeg")
bgr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized = cv2.resize(bgr, IMG_SIZE)

net = Net()
net.load_state_dict(torch.load("VarroaModel.pth"))
net.eval()
result = net(Tensor(resized))
print(result)
