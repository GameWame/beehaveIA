import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):

    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=2, stride=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.bn2 = nn.BatchNorm2d(64)
        self.bn3 = nn.BatchNorm2d(128)
        self.fc1 = None
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 2)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.bn1(self.conv1(x))), (3, 3))
        x = F.max_pool2d(F.relu(self.bn2(self.conv2(x))), (3, 3))
        x = F.max_pool2d(F.relu(self.bn3(self.conv3(x))), (2, 2))

        to_linear = x[0].shape[0]*x[0].shape[1]*x[0].shape[2]
        x = x.view(-1, to_linear)

        self.fc1 = nn.Linear(to_linear, 128)

        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))

        return F.softmax(x, dim=1)
