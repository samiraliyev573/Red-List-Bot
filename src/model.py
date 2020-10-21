import torch
import torch.nn as nn

class NeuralNet(nn.Module):

    def __init__(self, input_size, hidden_size, num_classes):
        # super method
        super(NeuralNet, self).__init__()
        # 3 linear layers
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l1 = nn.Linear(hidden_size, hidden_size)
        self.l1 = nn.Linear(hidden_size, num_classes)

        #activation function
        self.relu = nn.ReLU()

    #implement forward path
    def forward(self, x):
        # first linear layer
        out = self.l1(x)
        out =self.relu(out)
        # second linear layer
        out = self.l2(out)
        out = self.relu(out)
        # third linear layer
        out = self.l3(out)
        return out



