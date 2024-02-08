# latihan looping buat segitiga

sisi = 10

# pake for
# dummy variable
print("awal for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
    
print("akhir for\n")
# 2. pake while

print("awal while")
count = 1
while True:
    print("*"*count)
    count += 1
    
    if count > sisi:
        break
print("akhir while")
    
    
# 3. cuma ganjil
print("awal while")
count = 1
while True:
    if (count%2):
        # ini akan print jika ganjil atau dilewatkan
        print("*"*count)
        count += 1
    else:
        # akan kembali jika ganjil
        count += 1
        continue
    
    # akan break jika count melibihi sisi
    if count > sisi:
        break    
 
    
print("akhir while")

# 4. cuma ganjil
print("awal while")
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        # ini akan print jika ganjil atau dilewatkan
        print(" "*spasi,"*"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali jika ganjil
        count += 1
        continue
    
    # akan break jika count melibihi sisi
    if count > sisi:
        break    
 
    
print("akhir while\n\n")

print("tugas ketupat")
print("awal while")
count = 1
count_2 = int(sisi/count)
spasi = int(sisi/2)
while True:
    if (count%2):
        # ini akan print jika ganjil atau dilewatkan
        print(" "*spasi,"*"*count)
        spasi -= 1
        count += 1
        
    elif (count_2%2):
        print("*"*count_2," "*spasi)
        spasi += 1
        count_2 += 1
    else:
        # akan kembali jika ganjil
        count_2 += 1
        continue
    
    # akan break jika count melibihi sisi
    if count > sisi:
        break    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    