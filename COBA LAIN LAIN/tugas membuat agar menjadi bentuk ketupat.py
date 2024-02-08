# tugas buat menjadi ketupat

sisi = 9

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

#bawahnya
count = count - 2
spasi = 1
while True:
    if (count%2):
        print(" "*spasi,"*"*count)
        spasi += 1
        count -= 1
        
    else:
        count -= 1
        continue
    
    if count == 0:
        break
    
        
 
    
print("akhir while")