import torch
from torch import nn
from env import env

device = torch.device("cuda")
    
model = nn.Sequential(
            nn.Linear(2, 2)
        )

optim = torch.optim.SGD(model.parameters(), lr=0.1)
game = env()
loss, x, y, = game.step(1, 1)
coords = torch.Tensor([x, y])

while True:
    ans = model(coords)
    loss, x, y = game.step(ans[0].item(), ans[1].item())
    optim.step()
    coords = torch.Tensor([x, y])