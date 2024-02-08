# setiap hasil dari operasi komperasi adalah boolean true/false

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print("==LEBIH BESAR DARI (>)==")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 6
print(b,'>',6,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# lebih kurang dari <
print("==LEBIH KURANG DARI (<)==")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 6
print(b,'<',6,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan >=
print("==LEBIH DARI SAMA DENGAN (>=)==")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 6
print(b,'>=',6,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan <=
print("==KURANG DARI SAMA DENGAN (<=)==")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 6
print(b,'<=',6,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)


# sama dengan (==)
print("== SAMA DENGAN (==) ==")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

# sama dengan (!=)
print("== TIDAK SAMA DENGAN (!=) ==")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# 'is' sebagai komparasi object
print("== OBJECT IDENTITY (IS)==")
x = 7 # assiignment membuat object
y = 7
print("nilai x",x,"id =",hex(id(x)))
print("nilai y",y,"id =",hex(id(y)))
hasil = x is y
print("x is y =",hasil)

x = 7 # assiignment membuat object
y = 8
print("nilai x",x,"id =",hex(id(x)))
print("nilai y",y,"id =",hex(id(y)))
hasil = x is y
print("x is y =",hasil)

# 'is not' sebagai komparasi object
print("== OBJECT IDENTITY (IS not)==")
x = 7 # assiignment membuat object
y = 7
print("nilai x",x,"id =",hex(id(x)))
print("nilai y",y,"id =",hex(id(y)))
hasil = x is not y
print("x is not y =",hasil)

x = 7 # assiignment membuat object
y = 8
print("nilai x",x,"id =",hex(id(x)))
print("nilai y",y,"id =",hex(id(y)))
hasil = x is not y
print("x is not y =",hasil)



