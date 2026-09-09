import torch
import ast
x = ast.literal_eval(input("enter a tensor"))
x = torch.tensor(x)
y = ast.literal_eval(input("enter another tensor"))
y = torch.tensor(y)
print(f"your tesnors are {x} and {y}")
