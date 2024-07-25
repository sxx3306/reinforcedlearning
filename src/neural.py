import torch
from torch import nn
from env import env
import time

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = nn.Sequential(
    nn.Linear(2, 2)
).to(device)

optim = torch.optim.SGD(model.parameters(), lr=0.001)
game = env()
reward, x, y = game.step(1, 1)

# Створення координат з requires_grad=True
coords = torch.tensor([x, y], dtype=torch.float32, device=device, requires_grad=True)

while True:
    action = model(coords)
    reward, x, y = game.step(action[0].item(), action[1].item())

    # Використання винагороди як помилки
    loss = torch.tensor(reward, dtype=torch.float32, device=device, requires_grad=True)

    print(loss, action, game.steps)

    optim.zero_grad()
    loss.backward()
    optim.step()

    coords = torch.tensor([x, y], dtype=torch.float32, device=device, requires_grad=True)

    time.sleep(0.1)
