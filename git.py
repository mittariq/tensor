import torch
import ast

x = ast.literal_eval(input("enter a tensor"))

print(f"your tesnor is {torch.tensor(x)}")

