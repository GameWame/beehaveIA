import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):

    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1)
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1)
        self.conv3 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=2, stride=1)
        self.conv4 = nn.Conv2d(in_channels=256, out_channels=512, kernel_size=1, stride=1)
        self.bn1 = nn.BatchNorm2d(64)
        self.bn2 = nn.BatchNorm2d(128)
        self.bn3 = nn.BatchNorm2d(256)
        self.bn4 = nn.BatchNorm2d(512)
        self.fc1 = nn.Linear(512, 2)

    def forward(self, x):

        x = F.max_pool2d(F.relu(self.bn1(self.conv1(x))), 3)

        x = F.max_pool2d(F.relu(self.bn2(self.conv2(x))), 3)

        x = F.max_pool2d(F.relu(self.bn3(self.conv3(x))), 3)

        x = F.max_pool2d(F.relu(self.bn4(self.conv4(x))), 1)

        to_linear = x[0].shape[0] * x[0].shape[1] * x[0].shape[2]
        x = x.view(-1, to_linear)

        x = F.relu(self.fc1(x))
        return F.softmax(x, dim=1)
