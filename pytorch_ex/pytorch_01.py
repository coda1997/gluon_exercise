from __future__ import print_function
import torch
from torch.autograd import Variable
x = torch.empty(5, 3)
print(x)

x = torch.rand(5, 3)
print(x)

x = torch.zeros(5, 3, dtype=torch.long)
print(x)

x = torch.IntTensor([123,123])
print(x)

x = Variable(torch.randn(5, 5))
y = Variable(torch.randn(5, 5))
z = Variable(torch.randn(5, 5), requires_grad=True)

a = x+y
print(a.requires_grad)

b = a+z
print(b.requires_grad)
