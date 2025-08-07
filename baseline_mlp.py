import torch
import torch.nn as nn

# --- Configurable Baseline MLP ---
class BaselineMLP(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim=128, num_layers=2):
        super().__init__()
        self.num_layers = max(1, num_layers) # Ensure at least one hidden layer
        self.hidden_dim = hidden_dim
        layers = []
        # First hidden layer
        layers.append(nn.Linear(input_dim, hidden_dim))
        layers.append(nn.ReLU())
        # Additional hidden layers
        for _ in range(self.num_layers - 1):
            layers.append(nn.Linear(hidden_dim, hidden_dim))
            layers.append(nn.ReLU())
        # Output layer
        layers.append(nn.Linear(hidden_dim, output_dim))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x)
# --- End Configurable Baseline MLP ---
