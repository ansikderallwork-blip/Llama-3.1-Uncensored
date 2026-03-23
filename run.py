import torch
import torch.nn as nn
import torch.optim as optim

model = torch.load('model')
model.eval()

while True:
    input = input("Enter a prompt: ")
    output = model(input)
    print(output)
