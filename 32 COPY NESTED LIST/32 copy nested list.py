data_0 = [1,2]
data_1 = [3,4]

list_2D = [data_0,data_1,10]
list_2d_copy = list_2D.copy()

print(f"data = {list_2D}")
print(f"data copy = {list_2d_copy}")

# mengambil

data = list_2D[0][1]
print(f"data = {data}")

# address semuanya
print(f"address data 2D asli = {hex(id(list_2D))}")
print(f"address data 2D copy = {hex(id(list_2d_copy))}")

print(f"address dari member ke-1")
print(f"address data 2D asli = {hex(id(list_2D[0]))}")
print(f"address data 2D copy = {hex(id(list_2d_copy[0]))}")


data = list_2D[0][1] = 3
data = list_2D[2] = 9
print(f"data = {list_2D}")
print(f"data copy = {list_2d_copy}")

# pake deepcopy
from copy import deepcopy

list_2D = [data_0,data_1,10]
list_2D_deepcopy = deepcopy(list_2D)

print(f"address data  asli = {hex(id(list_2D))}")
print(f"address data deepcopy = {hex(id(list_2D_deepcopy))}")

print(f"address dari member ke-1")
print(f"address data  asli = {hex(id(list_2D[0]))}")
print(f"address data deepcopy = {hex(id(list_2D_deepcopy[0]))}")

data = list_2D[0][1] = 30

print(f"data = {list_2D}")
print(f"data copy = {list_2d_copy}")
print(f"data deepcopy = {list_2D_deepcopy}")

