import torch
import ast
x = ast.literal_eval(input("enter a tensor"))
x = torch.tensor(x)
y = ast.literal_eval(input("enter another tensor"))
y = torch.tensor(y)
print(f"your tesnors are {x} and {y}")
o= input("enter operation add, subtract, multiply")
try : 
  if "add" in o:
    print(f"tensor addition is {x + y}")
  if "sub" in o:
    print(f"tensor subtraction is {x - y}")
  if "mul" in o:
    print(f"tensor multipltion is {x @ y}")
except:
  print("error")
  
