import torch

from cnn import train

net = train()
torch.save(net.state_dict(), "./VarroaModel.pth")
