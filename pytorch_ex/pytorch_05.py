import torch
import torch.nn

# dtype = torch.float
# device = torch.device("cuda:0")

N, D_in, H, D_out = 64, 1000, 100, 10
x = torch.randn(N, D_in).cuda()
y = torch.randn(N, D_out).cuda()

model = torch.nn.Sequential(
    torch.nn.Linear(D_in, H),
    torch.nn.ReLU(),
    torch.nn.Linear(H, D_out),
).cuda()


loss_fn = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-4

for t in range(50000):
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    if t % 1000 == 0:
        print(t, loss)

    model.zero_grad()
    loss.backward()

    with torch.no_grad():
        for param in model.parameters():
            param -= learning_rate * param.grad
