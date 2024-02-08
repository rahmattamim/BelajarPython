# not, or , and , xor

# not
print("== NOT ==")
a = True
c = not a
print("data a =",a)
print("----not")
print("data c =",c)

# or
# jika salah satu true jadi true semua

print("== NOT ==")
a = True
b = False
c = a or b
print(a,'OR',b,' =',c)

a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

a = True
b = True
c = a or b
print(a,'OR',b,'  =',c)

a = False
b = True
c = a or b
print(a,'OR',b,' =',c)

# and
# jika dua nilai true jadi true 

print("== AND ==")
a = True
b = False
c = a and b
print(a,'AND',b,' =',c)

a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

a = True
b = True
c = a and b
print(a,'AND',b,'  =',c)

a = False
b = True
c = a and b
print(a,'AND',b,' =',c)

# xor
# jika salah satu true dia jadi true 
# kalo true sama true jadi false

print("== XOR ==")
a = True
b = False
c = a ^ b
print(a,'XOR',b,' =',c)

a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = True
c = a ^ b
print(a,'XOR',b,'  =',c)

a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)