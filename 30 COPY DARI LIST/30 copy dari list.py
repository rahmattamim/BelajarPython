## teknik menduplikat list

a = ["Ucup","Otong","Dudung"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# kita akan merubah member dari a

# ini akan merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengab copy
print("membuat list c dengan a.copy()")
c = a.copy() # duplikatnya/data baru

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("merubah data c")
c[0] = "Mamat"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")