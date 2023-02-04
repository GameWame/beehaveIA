import torch


class Net(torch.nn.Module):

    def __init__(self):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(1, 64, 3)
        self.conv2 = torch.nn.Conv2d(64, 512, 3)
        self.conv3 = torch.nn.Conv2d(512, 1024, 3)

        self.fc1 = None
        self.fc2 = torch.nn.Linear(512, 512)
        self.fc3 = torch.nn.Linear(512, 2)

    def forward(self, x):
        x = torch.nn.functional.max_pool2d(torch.nn.functional.relu(self.conv1(x)), (2, 2))
        x = torch.nn.functional.max_pool2d(torch.nn.functional.relu(self.conv2(x)), (2, 2))
        x = torch.nn.functional.max_pool2d(torch.nn.functional.relu(self.conv3(x)), (2, 2))

        to_linear = x[0].shape[0]*x[0].shape[1]*x[0].shape[2]
        x = x.view(-1, to_linear)

        self.fc1 = torch.nn.Linear(to_linear, 512)

        x = torch.nn.functional.relu(self.fc1(x))
        x = torch.nn.functional.relu(self.fc2(x))
        x = torch.nn.functional.relu(self.fc3(x))

        return torch.nn.functional.softmax(x, dim=1)
